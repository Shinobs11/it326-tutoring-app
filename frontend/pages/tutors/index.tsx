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
  ButtonGroup
}
from "@chakra-ui/react";
import { userArrayByTutor } from '../../sampleData';


const TutorIndex:NextPage = () =>{
  return (
    <Box>
      <Navbar/>
      <Text>
        Tutor index
      </Text>
    </Box>
  )
}

export default TutorIndex;