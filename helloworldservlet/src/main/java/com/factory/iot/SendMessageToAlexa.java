package com.factory.iot;

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

public class SendMessageToAlexa {
	public static MessageBean send(MessageBean msg) throws UnknownHostException, IOException, InterruptedException {

		ObjectMapper mapper = new ObjectMapper();
		MessageBean bean = null;
		Socket sock = new Socket("anilexa.com", 11002);
		BufferedWriter writerRasp = new BufferedWriter(new OutputStreamWriter(sock.getOutputStream()));
		BufferedReader readerRasp = new BufferedReader(new InputStreamReader(sock.getInputStream()));
		System.out.println("Trying to write command to socket " + mapper.writeValueAsString(msg));

		writerRasp.write(mapper.writeValueAsString(msg) + "\n");
		System.out.println("Write to server complete");
		writerRasp.flush();
		System.out.println("Waiting for response from server");
		String response = readerRasp.readLine();
		System.out.println(response);
		sock.close();

		bean = mapper.readValue(response, MessageBean.class);
		// command=scan.nextLine();

		return bean;

	}

}
