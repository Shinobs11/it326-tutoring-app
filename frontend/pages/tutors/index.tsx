import * as React from 'react';
import { useState, useEffect } from 'react';
import type { NextPage } from 'next'
import Head from 'next/head'
import Navbar from '../../components/Navbar/Navbar';
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
import { userArrayByTutor } from '../../sampleData';
import { User } from '../../classes';


interface TutorListItemProps{
  user: User
}
interface TutorListProps {
  userList: Array<User>;
}



const UserListItem:React.FunctionComponent<TutorListItemProps> = ({user, ...props}: TutorListItemProps)=>{
  const userName: string = `${user.firstName} ${user.lastName}`;
  return (
    <Tr
    _hover={{
      bg: ''
    }}
    >
      <Td>
        <Avatar
        zIndex={0}
          name={userName}
          size='xs'
        ></Avatar>
      </Td>
      <Td
      
      >
        {userName}
      </Td>
    </Tr>
  )
}

const UserList:React.FunctionComponent<TutorListProps> = ({userList,...props}:TutorListProps) =>{
  return (
        <Table
        >
          <Thead zIndex={1} top={0} position={'sticky'} bg='red.600'>
            <Tr>
              <Th></Th>
              <Th textColor={'white'}>
                Name
              </Th>

            </Tr>
          </Thead>
          <Tbody>       
            {
              userList.map((user)=><UserListItem user={user}/>)
            }
          </Tbody> 
        </Table>
  )
}



const TutorIndex:NextPage = () =>{




  return (
    <Box>
      <Navbar/>
      <Center>
        <Box
        
        bg={"white"}
        minW={'5xl'}
        maxHeight={'calc(100vh - 64px)'}
        overflowY='auto'
        my={'0.5rem'}
        >
          <UserList  userList={userArrayByTutor}/>
        </Box>
      </Center>
    </Box>
  )
}

export default TutorIndex;