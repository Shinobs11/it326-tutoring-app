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
const Home: NextPage = () => {
  return (
    <Box>
      <Head>
        <title>Tutor Tim</title>
        <meta name="viewport" content="initial-scale=1.0, width=device-width" />
      </Head>
      <Navbar/>
      <Center>
        <Box 
          h={'calc(100vh - 64px)'}
          justifyContent={'center'}
          alignItems={'center'}
          display='flex'
          w='5xl'
          >
          <VStack spacing={6}>
            <Link href={"/signup"}>
              <ThemeButton>
                Sign Up
              </ThemeButton >
            </Link>
            <Link href={"/login"}>
              <ThemeButton>
                Log In
              </ThemeButton>
            </Link>
          </VStack>

        </Box>
      </Center>
    </Box>
  )
}

export default Home
