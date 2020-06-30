package com.server;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.net.ServerSocket;
import java.net.Socket;

import com.bean.MessageBean;
import com.fasterxml.jackson.databind.ObjectMapper;

public class AlexaServer implements Runnable {
	private ServerSocket listenerAlexa;
	private Socket socketAlexa;
	private PiServer piServ;

	public AlexaServer(PiServer piServ) throws IOException {
		this.listenerAlexa = new ServerSocket(11002);
		this.piServ = piServ;
	}

	public boolean isConnected() {
		return piServ.isConnected();
	}

	@Override
	public void run() {
		while (true) {
			try {
				socketAlexa = listenerAlexa.accept();
				System.out.println("Connection established with Alexa");

				BufferedWriter writerAlexa = new BufferedWriter(new OutputStreamWriter(socketAlexa.getOutputStream()));
				BufferedReader readerAlexa = new BufferedReader(new InputStreamReader(socketAlexa.getInputStream()));

				System.out.println("Waiting for command from alexa");
				String commandFromLexa = readerAlexa.readLine();
				System.out.println("Got following command from alexa: " + commandFromLexa);

				ObjectMapper mapper = new ObjectMapper();
				MessageBean bean = mapper.readValue(commandFromLexa, MessageBean.class);
				if(isConnected()) {
					System.out.println("Found connected with Pi trying to send message");
					MessageBean beanPi = piServ.talkwithPi(bean);
					// write data to raspberry pi
					writerAlexa.write(mapper.writeValueAsString(beanPi) + "\n");
					writerAlexa.flush();
					writerAlexa.close();
					readerAlexa.close();
					socketAlexa.close();
				}else {
					bean.setOutMSG("Pi not connected");
					// write data to raspberry pi
					writerAlexa.write(mapper.writeValueAsString(bean) + "\n");
					writerAlexa.flush();
					writerAlexa.close();
					readerAlexa.close();
					socketAlexa.close();
				}
				
				
			} catch (Exception exc) {
				exc.printStackTrace();
			}

		}

	}
}
