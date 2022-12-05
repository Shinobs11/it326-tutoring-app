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
  Image,
  Icon,
  Center,
  Link,
  VStack
}
from "@chakra-ui/react";
import ThemeButton from '../components/ThemeButton/ThemeButton';
import { NextPage } from 'next';



const Inbox:NextPage = () =>{
  return (
    <Box>
      <Navbar/>
      <Box
      h={'calc(100vh - 64px)'}
      w='5xl'
      >
        <Center>
            To be determined. (might use a grid for this instead of a table like I've been doing with everything else)
            Turns out tables are really bad at doing a-lot thing that aren't explicitly related to displaying data in a tabular format.
        </Center>
      </Box>

    </Box>
  )
} 

export default Inbox;