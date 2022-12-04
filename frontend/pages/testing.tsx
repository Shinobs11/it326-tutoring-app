import * as React from 'react';
import { useState, useEffect } from 'react';
import type { NextPage } from 'next'
import Head from 'next/head'
import Navbar from '../components/Navbar/Navbar';
import Schedule from '../components/Schedule/Schedule';
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
  Wrap,
  WrapItem
}
from "@chakra-ui/react";
import SignupForm from '../components/SignupForm/SignupForm';


const Testing:NextPage = ()=>{



return (
  <>
  {/* <Wrap>

  </Wrap> */}
  <SignupForm></SignupForm>
  </>
)

}

export default Testing;