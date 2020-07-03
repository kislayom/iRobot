package com.simulator;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.net.ServerSocket;
import java.net.Socket;

public class ServerSim {
	public static void main(String args[]) throws IOException {
		ServerSocket listenerPi;
		listenerPi = new ServerSocket(11001);
		Socket socketPi = listenerPi.accept();
		System.out.println("Pi Connected!!");
		BufferedReader readerPi = new BufferedReader(new InputStreamReader(socketPi.getInputStream()));
		BufferedWriter writerPi = new BufferedWriter(new OutputStreamWriter(socketPi.getOutputStream()));
		
		while(true) {
		writerPi.write("hello Pi! \n");
		//writerPi.newLine();
		writerPi.flush();
		
		}
		
		
	}
}
