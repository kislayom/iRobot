package com.server;

import java.io.IOException;
import java.net.ServerSocket;

public class PlutoServerMain {
	public static void main(String args[]) throws IOException {
		// Start 2 threads which should hold reference connections in main class
		// each thread should connect individually to alexa and pi each

		PiServer piServer = new PiServer();
		AlexaServer alexaServer= new AlexaServer(piServer);
		piServer.setAlexaServ(alexaServer);
		
		Thread tPi= new Thread(piServer);
		Thread tAlexa= new Thread(alexaServer);
		
		tPi.start();
		tAlexa.start();
		
		try {
			tPi.join();
			tAlexa.join();
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		
		System.out.println("Quitting Program");
		
	}

}
