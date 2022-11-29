import * as React from 'react';
import { useState, useEffect } from 'react';
import {
  Box,
  Flex,
  Text,
  useColorModeValue,
  Button,
  Stack,
  Heading,
  Container,
  Link,
  Image,
  Icon,
  Center,
  List,
  ListIcon,
  ListItem,
  ListItemProps,
  ListProps,
  HStack
}
from "@chakra-ui/react";

import {Session, Tutor} from '../../classes'


interface SchedulePropsType {
  children?: React.ReactNode;
  sessions: Session[]
}
interface ScheduleItemPropsType{
  children?: React.ReactNode;
  session: Session
}
const ScheduleItem = ({session, ...props}:ScheduleItemPropsType) =>{
  return (
    <HStack spacing={4} maxH="2.5rem">
      <Text>
        {session.startTime.toLocaleString()}
      </Text>
      <Text>
        {session.title}
      </Text>
    </HStack>
  )
}

const Schedule = ({sessions,...props}:SchedulePropsType) =>{
  return (  
    <Container>
      <List>
        {
          sessions.map(
            (session)=>{
              return (
                <ListItem>

                </ListItem>
              )
            }
          )
        }
      </List>
    </Container>
  
    )
}

export default Schedule;