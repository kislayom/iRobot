package com.server;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.net.ServerSocket;
import java.net.Socket;

import javax.sound.midi.Soundbank;

import com.bean.MessageBean;
import com.fasterxml.jackson.databind.ObjectMapper;

public class PiServer implements Runnable {

	private ServerSocket listenerPi;
	private Socket socketPi;
	private AlexaServer alexaServ;
	private String OUTPUT;

	public PiServer() throws IOException {
		this.listenerPi = new ServerSocket(11001);
		OUTPUT = "NA";
	}

	public void setAlexaServ(AlexaServer alexaServ) {
		this.alexaServ = alexaServ;
	}

	public boolean isConnected() {
		return (socketPi != null) ? true : false;
	}

	@Override
	public void run() {
		while (true) {
			try {
				socketPi = listenerPi.accept();
				System.out.println("Pi Connected!!");
				BufferedReader readerPi = new BufferedReader(new InputStreamReader(socketPi.getInputStream()));

				OUTPUT = readerPi.readLine();
				while (OUTPUT != null) {
					System.out.println("Pi Server received " + OUTPUT);
				}
				OUTPUT = readerPi.readLine();

				if (OUTPUT == null) {
					socketPi = null;
					OUTPUT = "NA";
				}

			} catch (IOException e) {
				// TODO Auto-generated catch block
				socketPi = null;

			}

		}
	}

	public MessageBean talkwithPi(MessageBean bean) throws IOException {
		System.out.println("PiServer : Got message from Alexa on pi " + bean);
		if (isConnected()) {
			System.out.println("PiServer : Connected state " + bean);

			BufferedWriter writerPi = new BufferedWriter(new OutputStreamWriter(socketPi.getOutputStream()));

			System.out.println("PiServer :  Stream initiated");
			ObjectMapper mapper = new ObjectMapper();
			System.out.println(mapper.writeValueAsString(bean) + "\n\r");
			writerPi.write(mapper.writeValueAsString(bean) + "\n\r");
			System.out.println("PiServer :  Completed writting to Pi");

			// MessageBean beanPi = mapper.readValue(responseFromPi, MessageBean.class);
			return bean;
		} else {
			System.out.println("PiServer : disconnected state " + bean);
			bean.setOutMSG("PiServer : Pi is not connected!");
			return bean;
		}
	}

}
