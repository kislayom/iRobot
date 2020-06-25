package com.server;

import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.HashMap;
import java.util.concurrent.ArrayBlockingQueue;
import java.util.concurrent.BlockingQueue;
import java.util.concurrent.ConcurrentHashMap;

public class ServerMain {

	
	static ServerSocket socketRaspberryPi=null;
	static ServerSocket socketAlexaService=null;
	
	
	
	public static void main(String args[]) throws IOException, ClassNotFoundException, InterruptedException {
		System.out.println("ServerMain: Attempting to start server at port 11001");
		ServerSocket listener = new ServerSocket(11001);		
		System.out.println("ServerMain: Job thread started");
		System.out.println("ServerMain: Server Started at 11001");
		
		while (true) {

			System.out.println("waiting for client to connect");
			Socket socketRaspberryPi = listener.accept();
			
			
			System.out.println("ServerMain: Client connected " + socketRaspberryPi.getRemoteSocketAddress());
			Thread thread = new Thread(new ServerHandler(socketRaspberryPi));
			thread.start();
			System.out.println("ServerMain: Client service started");
			//Thread.sleep(1000);
		}
	}

}