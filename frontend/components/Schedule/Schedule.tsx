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
  HStack,
  Table,
  Thead,
  Tbody,
  Tfoot,
  Tr,
  Th,
  Td,
  TableCaption,
  TableContainer,
}
from "@chakra-ui/react";
import { Card, CardHeader, CardBody, CardFooter } from '@chakra-ui/react'
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
    // <HStack maxH="2.5rem">
    //   <Card bgColor="red.200">
    //     <CardBody display={"flex"} flexDirection={"row"}>
    //       <Text width={'7rem'}>
    //         {session.startTime.toLocaleDateString()}
    //       </Text>
    //       <Text>{ 
    //         `${session.startTime.toLocaleTimeString()} - ${session.endTime.toLocaleTimeString()}`
    //       }
    //       </Text>
    //       <Text>
    //         {session.title}
    //       </Text>
    //     </CardBody>
    //   </Card>
    // </HStack>
    <Tr>
      <Td>
        {session.startTime.toLocaleDateString()}
      </Td>
      <Td>
        {session.startTime.toLocaleTimeString()}
      </Td>
      <Td>
        {session.title}
      </Td>
    </Tr>
  )
}

const Schedule = ({sessions,...props}:SchedulePropsType) =>{
  const [isHydrated, setHydrated] = useState<boolean>(false);
  useEffect(()=>{ 
    setHydrated(true);
  }, []);

  if(isHydrated){
  return (  
    <Container>
      <Text fontSize={24} fontWeight={600}>
        My sessions
      </Text>
      <TableContainer>
        <Table>
          <Thead>
            <Tr>
              <Th>Date</Th>
              <Th>Time</Th>
              <Th>Title</Th>
            </Tr>
          </Thead>
          <Tbody>
          {
            sessions.map((session)=>{
              return(
              <ScheduleItem session={session}/>
              )
            })
          }
          </Tbody>
        </Table>
      </TableContainer>
    
    </Container>
  
    )}
    else {
      return (
        <>
        </>
      )
    }
}

export default Schedule;