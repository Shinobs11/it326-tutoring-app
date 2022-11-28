import * as React from 'react';
import { useState, useEffect } from 'react';
import type { NextPage } from 'next'
import Head from 'next/head'
import Navbar from '../components/Navbar/Navbar';
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
  HStack
}
from "@chakra-ui/react";

const Dashboard: NextPage = () =>{
  return (
    <Box height="100vh">
      <Head>
        <title>Dashboard | Tutor Tim</title>
        <meta name="viewport" content="initial-scale=1.0, width=device-width" />
      </Head>
      <Navbar/>
    
        <HStack>
          <VStack
            minW='xs'
            minHeight={'calc(100vh - 64px)'}
            backgroundColor='blue.200'
            height="100%" 
            justify='flex-start'
            >
            <Avatar
              my="2rem"
              name="Placeholder Name"
              size='xl'
            >
            </Avatar>
            <Text>
              Placeholder bio
            </Text>
          </VStack>
          <Divider orientation='vertical'/>
          <VStack
            minHeight={'calc(100vh - 64px)'}
            backgroundColor='green.200'
          >
            <Text>
              Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
            </Text>
          </VStack>
        </HStack>
        
    </Box>
  )
}
export default Dashboard;


