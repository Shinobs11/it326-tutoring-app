import * as React from 'react';
import { useState, useEffect } from 'react';
import { useRouter } from 'next/router';
import type { NextPage } from 'next'
import Head from 'next/head'
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
import Navbar from '../../components/Navbar/Navbar';





const TutorProfile:NextPage = () =>{

  const router = useRouter();
  const {tutorId} = router.query;


  return (
  <Box>
    <Navbar/>
    <Text>
      {tutorId}
    </Text>
  </Box>
  )
}
export default TutorProfile;