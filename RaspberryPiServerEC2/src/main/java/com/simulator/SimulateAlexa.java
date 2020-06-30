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

public class SimulateAlexa {
	public static void main(String args[]) throws UnknownHostException, IOException, InterruptedException {

		Scanner scan = new Scanner(System.in);
		
		System.out.println("Type command");
		String command = scan.nextLine();
		System.out.println("Command recived: "+command);
		while (!command.equalsIgnoreCase("exit")) {
			Socket sock = new Socket("192.168.0.101", 11002);
			BufferedWriter writerRasp = new BufferedWriter(new OutputStreamWriter(sock.getOutputStream()));
			BufferedReader readerRasp = new BufferedReader(new InputStreamReader(sock.getInputStream()));
			System.out.println("Trying to write command to socket "+command);
			
			ObjectMapper mapper = new ObjectMapper();
			String json="{\"action\":\"MVS\",\"timeStamp\":1592130955041,\"value\":\"1\",\"outDist\":\"20\",\"outTemp\":\"\",\"outHumid\":\"\"} \n";
			MessageBean bean = mapper.readValue(json, MessageBean.class);
			writerRasp.write(mapper.writeValueAsString(bean)+"\n");
			System.out.println("Write to server complete");
			writerRasp.flush();
			System.out.println("Waiting for response from server");
			String response=readerRasp.readLine();
			System.out.println(response);
			sock.close();
			Thread.sleep(2000);
			//command=scan.nextLine();
		}

	}

}
