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
  Center
}
from "@chakra-ui/react";
const Home: NextPage = () => {
  return (
    <div>
      <Head>
        <title>Tutor Tim</title>
        <meta name="viewport" content="initial-scale=1.0, width=device-width" />
      </Head>
      <Navbar/>
      <Box bg={useColorModeValue('red.50', 'red.50')} px={4}>
      

      </Box>
    </div>
  )
}

export default Home
