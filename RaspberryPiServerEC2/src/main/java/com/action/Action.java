package com.action;

import java.io.IOException;

import com.bean.MessageBean;
import com.fasterxml.jackson.core.JsonParseException;
import com.fasterxml.jackson.databind.JsonMappingException;
import com.fasterxml.jackson.databind.ObjectMapper;

public abstract class Action {

	MessageBean bean;

	public Action(String json) {
		try {
			ObjectMapper mapper = new ObjectMapper();
			MessageBean bean = mapper.readValue(json, MessageBean.class);
			this.bean = bean;
		} catch (Exception exc) {
			System.out.println(exc);
		}

	}

	public Action(MessageBean bean) {
		this.bean = bean;
	}

	public abstract MessageBean process();
}
