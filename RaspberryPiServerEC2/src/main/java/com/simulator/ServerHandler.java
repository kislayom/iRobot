package com.simulator;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.io.OutputStreamWriter;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.Date;
import java.util.concurrent.BlockingQueue;
import java.util.concurrent.ConcurrentHashMap;

import com.bean.MessageBean;
import com.fasterxml.jackson.databind.ObjectMapper;

public class ServerHandler implements Runnable {
	Socket socket;

	ServerSocket listenerAlexa =null;

	public ServerHandler(Socket socket) throws IOException {
		this.socket = socket;
		// Listen to Alexa Services
		this.listenerAlexa = new ServerSocket(11002);

	}

	public void run() {
		String fileName = "";
		System.out.println("ServerHandler: Client handler started");
		File file = new File("");
		long lastMofidied = file.lastModified();

		try {
			// getting streams
			BufferedWriter writerRasp = new BufferedWriter(new OutputStreamWriter(socket.getOutputStream()));
			BufferedReader readerRasp = new BufferedReader(new InputStreamReader(socket.getInputStream()));
			ObjectMapper mapper = new ObjectMapper();

			// add the message to queue
			while (socket.isConnected()) {
				System.out.println("Waiting for connection from Alexa");
				Socket socketAlexa = listenerAlexa.accept();
				System.out.println("Connection established with Alexa");

				BufferedWriter writerAlexa = new BufferedWriter(new OutputStreamWriter(socketAlexa.getOutputStream()));
				BufferedReader readerAlexa = new BufferedReader(new InputStreamReader(socketAlexa.getInputStream()));

				System.out.println("Waiting for command from alexa");
				String commandFromLexa = readerAlexa.readLine();
				System.out.println("Got following command from alexa: " + commandFromLexa);
				// write data to raspberry pi
				writerRasp.write(commandFromLexa + "\n\r");
				System.out.println("Done writting to pi");
				writerRasp.flush();

				String returnMsg = readerRasp.readLine();
				System.out.println("Command from Pi"+returnMsg);
				writerAlexa.write(returnMsg+"\n");
				writerAlexa.flush();
				writerAlexa.close();
				readerAlexa.close();
				socketAlexa.close();
				

			}

		} catch (Exception exc) {
			System.out.println(exc);
			exc.printStackTrace();
		}
	}

}