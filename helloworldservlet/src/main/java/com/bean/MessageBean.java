package com.bean;


import java.util.Date;

import com.fasterxml.jackson.databind.ObjectMapper;

/**
 * @author kislay
 *
 */
public class MessageBean {
	String action;
	long timeStamp;
	String value;
	String outMSG;

//{"action":"MVS","timeStamp":1592130955041,"value":"1","outMSG":"20"}
	public MessageBean() {
		this.timeStamp=new Date().getTime();
		this.action="";
		this.value="";
		this.outMSG="";
		
	}
	public String getAction() {
		return action;
	}

	public void setAction(String action) {
		this.action = action;
	}

	public long getTimeStamp() {
		return timeStamp;
	}

	public void setTimeStamp(long timeStamp) {
		this.timeStamp = timeStamp;
	}

	public String getValue() {
		return value;
	}

	public void setValue(String value) {
		this.value = value;
	}
	public String getOutMSG() {
		return outMSG;
	}
	public void setOutMSG(String outMSG) {
		this.outMSG = outMSG;
	}



}
