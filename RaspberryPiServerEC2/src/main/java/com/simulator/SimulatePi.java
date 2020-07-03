package com.simulator;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.net.Socket;
import java.net.UnknownHostException;
import java.util.Scanner;

import com.bean.MessageBean;
import com.fasterxml.jackson.databind.ObjectMapper;

public class SimulatePi {
	public static void main(String args[]) throws UnknownHostException, IOException, InterruptedException {

		Socket sock = new Socket("anilexa.com", 11001);
		System.out.println("Connected with server");
		while (true) {

			BufferedWriter writerPi = new BufferedWriter(new OutputStreamWriter(sock.getOutputStream()));
			BufferedReader readerPi = new BufferedReader(new InputStreamReader(sock.getInputStream()));

			String command = readerPi.readLine();
			System.out.println("Found command " + command);
			ObjectMapper mapper = new ObjectMapper();
			MessageBean bean = mapper.readValue(command, MessageBean.class);
			bean.setOutMSG("Pi modified message : Kislay");
			writerPi.write(mapper.writeValueAsString(bean) + "\n");
			System.out.println("Write to server complete");

			writerPi.flush();
			System.out.println("completed writing from remote device");

			// Thread.sleep(2000);
			// command=scan.nextLine();
		}

	}

}
