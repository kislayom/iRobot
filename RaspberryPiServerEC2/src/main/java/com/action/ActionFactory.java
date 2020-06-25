package com.action;

import java.io.IOException;

import com.bean.MessageBean;
import com.fasterxml.jackson.core.JsonParseException;
import com.fasterxml.jackson.databind.JsonMappingException;
import com.fasterxml.jackson.databind.ObjectMapper;

//s.no	Command	command sent to pi	attributes input	attributes output
//Move Straight	MV		
//1	Move Straight x Seconds	MVS	time	
//2	move straight distance from front is more than x cms	MVSO	distance	
//3	move left x seconds	MVL	time	
//4	move right x seconds	MVR	time	
//5	move back x seconds	MVB	time	
//6	find distance front	FDF		
//7	find distance left	FDL		
//8	find distance right	FDR		
//9	find distance half left	FDHL		
//10	find distance half right	FDHR		
//11	turn on head light	HON		
//12	turn off head light	HOFF		
//13	turn on head light for x seconds	HONDUR		
//14	turn off head light after x seconds	HOFFDUR		
//15	find temperature	FTEM		
//16	find humidity	FHUM		
//17	find temperature and humidity	FTEMHUM		
//18	save picture	SNDPIC		
//19	save video	SNDVID		
//20	start automatic	STARTAUTO		
//21	stop automatic	STOPAUTO		
//22	dance	DANCESTART		
//23	dance and stop time	DANCESTARTDUR		
//STOP ALL	STOPALL		
//exit Bot	EXITBOT		

public class ActionFactory {

	public static final String MV = "MV";
	public static final String MVS = "MVS";
	public static final String MVSO = "MVSO";
	public static final String MVL = "MVL";
	public static final String MVR = "MVR";
	public static final String MVB = "MVB";
	public static final String FDF = "FDF";
	public static final String FDL = "FDL";
	public static final String FDR = "FDR";
	public static final String HON = "HON";
	public static final String HOFF = "HOFF";

	public static final String FTEM = "FTEM";
	public static final String FHUM = "FHUM";

	public static final String SNDPIC = "SNDPIC";
	public static final String SNDVID = "SNDVID";
	public static final String STARTAUTO = "STARTAUTO";

	public static final String DANCESTART = "DANCESTART";

	public static final String STOPALL = "STOPALL";
	public static final String EXITBOT = "EXITBOT";

	public Action getAction(String json) throws JsonParseException, JsonMappingException, IOException {
		ObjectMapper mapper = new ObjectMapper();
		MessageBean bean = mapper.readValue(json, MessageBean.class);
		Action action = null;
		switch (bean.getAction()) {
		case MV:
			action = new MoveStraightAction(bean);
			break;
		case MVS:
			action = new MoveStraightXSec(bean);
			break;
		case MVSO:
			action = new MoveStraightDistanceX(bean);
			break;
		case MVL:
			action = new MoveLeftX(bean);
			break;
		case MVR:
			action = new MoveRightX(bean);
			break;
		case MVB:
			action = new MoveBackX(bean);
			break;
		case FDF:
			action = new FindDistanceFront(bean);
			break;
		case FDL:
			action = new FindDistanceLeft(bean);
			break;
		case FDR:
			action = new FindDistanceRight(bean);
			break;
		case HON:
			action = new TurnOnHeadLight(bean);
			break;
		case HOFF:
			action = new TurnOffHeadLight(bean);
			break;

		case FTEM:
			action = new FindTemperature(bean);
			break;
		case FHUM:
			action = new FindHumidity(bean);
			break;

		case SNDPIC:
			action = new SavePicture(bean);
			break;
		case SNDVID:
			action = new SaveVideo(bean);
			break;
		case STARTAUTO:
			action = new StartAutomatic(bean);
			break;
		case DANCESTART:
			action = new Dance(bean);
			break;
		case STOPALL:
			action = new StopAll(bean);
			break;
		case EXITBOT:
			action = new ExitBot(bean);
			break;

		}

		return action;
	}

}
