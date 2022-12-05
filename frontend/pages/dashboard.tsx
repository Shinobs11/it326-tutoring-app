import * as React from 'react';
import { useState, useEffect } from 'react';
import type { NextPage } from 'next'
import Head from 'next/head'
import Navbar from '../components/Navbar/Navbar';
import Schedule from '../components/Schedule/Schedule';
import Profile from '../components/Profile/Profile';
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
  Avatar,
  VStack,
  Divider,
  HStack,
  ButtonGroup,
  useDisclosure,
  Modal,
  ModalOverlay,
  ModalContent,
  ModalHeader,
  ModalFooter,
  ModalBody,
  ModalCloseButton,
  FormControl,
  FormLabel,
  Input,
}
from "@chakra-ui/react";


import {sessionSample} from '../sampleData/sessionSample'
import TutoredSessions from '../components/TutoredSessions/TutoredSessions';


enum SelectedButtonEnum {
  PROFILE,
  TUTORING_SESSIONS,
  TUTOR_SESSIONS,
  ORG_MEMBER,
  ORG_MANAGE

}

interface ButtonInfoType {
  name: string;
  enumValue: number;
}

const ButtonInfo: ButtonInfoType[] = [
  {
    name: 'Profile',
    enumValue: SelectedButtonEnum.PROFILE
  },
  {
    name: 'Tutoring Sessions',
    enumValue: SelectedButtonEnum.TUTORING_SESSIONS
  },
  {
    name:'My Sessions',
    enumValue: SelectedButtonEnum.TUTOR_SESSIONS
  },
  {
    name: 'Org. Membership',
    enumValue: SelectedButtonEnum.ORG_MEMBER
  },
  {
    name: 'Manage Organizations',
    enumValue: SelectedButtonEnum.ORG_MANAGE
  }
]


const Dashboard: NextPage = () =>{
  const [activeDashButton, setActiveDashButton] = useState<SelectedButtonEnum>(0);
  const {isOpen, onOpen, onClose} = useDisclosure();

  const renderSelectedPage = () =>{
    switch(activeDashButton){
      case SelectedButtonEnum.PROFILE:
        return(
          <Profile 
            firstName='John'
            lastName='Doe'
            emailAddress='example@example.com'
            phoneNumber='555-555-5555'
          />
        )
       
      case SelectedButtonEnum.TUTORING_SESSIONS:
        return(
          <Schedule sessions={sampleSessions}/>
        )
      
      case SelectedButtonEnum.TUTOR_SESSIONS:
        

        return(
          <>
          <TutoredSessions sessions={sessionSample}/>
          <Button onClick={onOpen}>Add Session</Button>
          <Modal closeOnOverlayClick={true} isOpen={isOpen} onClose={onClose}>
            <ModalOverlay/>
            <ModalContent>
              <ModalHeader>Add Session</ModalHeader>
              <ModalCloseButton/>
              <ModalBody>
                <FormControl onSubmit={}>
                  <FormLabel>Title</FormLabel>
                  <Input/>
                  <FormLabel>Start Date</FormLabel>
                  <Input type='datetime-local'/>
                </FormControl>
              </ModalBody>
              <ModalFooter>
                <Button mr={3} onClick={onClose}>
                  Close
                </Button>
                <Button>
                  Add Session
                </Button>
              </ModalFooter>
            </ModalContent>

          </Modal>
          </>
        )
    }
  }
  

  const buttonList = ButtonInfo.map(
    (info)=>{
      return (
        <Button 
        isActive={info.enumValue == activeDashButton}
        onClick={(e)=>{setActiveDashButton(info.enumValue)}}
        minWidth={'3xs'}>
          {info.name}
        </Button>
      )
    }
  )


  return (
    <Box height="100vh" bgColor={'gray.100'}>
      <Head>
        <title>Dashboard | Tutor Tim</title>
        <meta name="viewport" content="initial-scale=1.0, width=device-width" />
      </Head>
      <Navbar/>
      <Center>
        <HStack bg='white' >
          <VStack
            minW='xs'
            minHeight={'calc(100vh - 64px)'}

            height="100%" 
            justify='flex-start'
            >
            <Avatar
              m="2rem"
              name="Placeholder Name"
              size='xl'
            >
            </Avatar>
            //default has profile button available
            <VStack>
              {
                buttonList
              }
            </VStack>
          </VStack>
          <Box
            height={'calc(100vh - 64px)'}
            bg='gray.100'
            zIndex={1}
            width={'2px'}
          ></Box>
          <VStack
            minHeight={'calc(100vh - 64px)'}
            minW={'4xl'}
          >
            {
              renderSelectedPage()
            }
          </VStack>
        </HStack>
        </Center>
    </Box>
  )
}
export default Dashboard;


