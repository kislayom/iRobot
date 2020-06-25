/*
     Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

     Licensed under the Apache License, Version 2.0 (the "License"). You may not use this file
     except in compliance with the License. A copy of the License is located at

         http://aws.amazon.com/apache2.0/

     or in the "license" file accompanying this file. This file is distributed on an "AS IS" BASIS,
     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for
     the specific language governing permissions and limitations under the License.
*/

package com.amazon.ask.helloworldservlet;

import com.amazon.ask.Skill;
import com.amazon.ask.Skills;
import com.amazon.ask.servlet.SkillServlet;

import com.amazon.ask.helloworldservlet.handlers.CancelandStopIntentHandler;
import com.amazon.ask.helloworldservlet.handlers.FindDistance;
import com.amazon.ask.helloworldservlet.handlers.HelloWorldIntentHandler;
import com.amazon.ask.helloworldservlet.handlers.HelpIntentHandler;
import com.amazon.ask.helloworldservlet.handlers.SessionEndedRequestHandler;
import com.amazon.ask.helloworldservlet.handlers.StartAutomatic;
import com.amazon.ask.helloworldservlet.handlers.Stop;
import com.amazon.ask.helloworldservlet.handlers.TurnOffHeadLight;
import com.amazon.ask.helloworldservlet.handlers.TurnOnHeadLight;
import com.amazon.ask.helloworldservlet.handlers.LaunchRequestHandler;
import com.amazon.ask.helloworldservlet.handlers.MoveBack;
import com.amazon.ask.helloworldservlet.handlers.MoveLeft;
import com.amazon.ask.helloworldservlet.handlers.MoveRight;
import com.amazon.ask.helloworldservlet.handlers.MoveStraight;

public class HelloWorldSkillServlet extends SkillServlet {

    public HelloWorldSkillServlet() {
        super(getSkill());
    }

    @SuppressWarnings("unchecked")
	private static Skill getSkill() {
        return Skills.standard()
                .addRequestHandlers(
                        new CancelandStopIntentHandler(),
                        new HelloWorldIntentHandler(),
                        new HelpIntentHandler(),
                        new LaunchRequestHandler(),
                        new SessionEndedRequestHandler(),
		                new MoveStraight(),
		                new MoveBack(),
		                new MoveLeft(),
		                new MoveRight(),
		                new FindDistance(),
		                new TurnOffHeadLight(),
		                new TurnOnHeadLight(),
		                new StartAutomatic(),
		                new Stop()
                )
                // Add your skill id below
                .withSkillId("amzn1.ask.skill.281a10f8-c235-42f3-ab67-746260df96cb")
                .build();
    }

}
