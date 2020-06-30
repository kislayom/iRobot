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

	public PiServer() throws IOException {
		this.listenerPi = new ServerSocket(11001);
	
	}
	
	public void setAlexaServ(AlexaServer alexaServ) {
		this.alexaServ = alexaServ;
	}

	public boolean isConnected() {
		return (socketPi != null && socketPi.isConnected()) ? true : false;
	}

	@Override
	public void run() {
		while (true) {
			try {
				socketPi = listenerPi.accept();
				System.out.println("Pi Connected!!");
				while (isConnected()) {
					Thread.sleep(300);
				}
				System.out.println("Pi Disconnected!!");

			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}

	}

	public MessageBean talkwithPi(MessageBean bean) throws IOException {
		System.out.println("Got message from Alexa on pi");
		if (isConnected()) {
			BufferedWriter writerRasp = new BufferedWriter(new OutputStreamWriter(socketPi.getOutputStream()));
			BufferedReader readerRasp = new BufferedReader(new InputStreamReader(socketPi.getInputStream()));

			ObjectMapper mapper = new ObjectMapper();
			writerRasp.write(mapper.writeValueAsString(bean) + "\n");
			String responseFromPi = readerRasp.readLine();
			MessageBean beanPi = mapper.readValue(responseFromPi, MessageBean.class);
			return beanPi;
		} else {
			MessageBean beanPi = new MessageBean();
			beanPi.setOutMSG("Pi is not connected!");
			return beanPi;
		}
	}

}
