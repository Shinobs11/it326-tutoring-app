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
  Image,
  Icon,
  Center,
  Avatar,
  VStack,
  Divider,
  HStack,
  Link,
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
  LinkBox,
  LinkOverlay
}
  from "@chakra-ui/react";
import NextLink from 'next/link';
import { useRouter } from 'next/router';
import { Session } from '../../classes';
import { sessionSample } from '../../sampleData/sessionSample';
import {ArrowRightIcon} from '@chakra-ui/icons'
interface SessionListItemProps {
  session: Session
}
interface SessionListProps {
  sessionList: Session[]
}



const SessionListItem: React.FunctionComponent<SessionListItemProps> = ({ session, ...props }: SessionListItemProps) => {
  const router = useRouter();
  return (
        <Tr
          _hover={{
            bg: 'gray.100'
          }}
        >
          <Td>
            {session.title}
          </Td>
          <Td>
            {session.startTime.toLocaleDateString()}
          </Td>
          <Td>
            {session.startTime.toLocaleTimeString()}
          </Td>
          <Td>
            {
              (session.classes.length <= 3) ?
                session.classes.map((c) => c.className).join(", ") :
                session.classes.slice(0, 3).map((c) => c.className).join(", ").concat("...")
            }
          </Td>
          <Td>
            {session.students.length}
          </Td>
          <Td>
            {session.capacity}
          </Td>
          <Td>
            <Link p={'4'} href={`/sessions/${session.sessionId}`}>
              <ArrowRightIcon/>
            </Link>
          </Td>

        </Tr>
  )
}

const SessionList: React.FunctionComponent<SessionListProps> = ({ sessionList, ...props }: SessionListProps) => {
  return (
    <Table
    
    >
      <Thead zIndex={1} top={0} position={'sticky'} bg='red.600'>
        <Tr>
          <Th textColor={'white'}>
            Title
          </Th>
          <Th textColor={'white'}>
            Start Date
          </Th>
          <Th textColor={'white'}>
            Start Time
          </Th>
          <Th textColor={'white'}>
            Classes
          </Th >
          <Th textColor={'white'}>
            Attendees
          </Th>
          <Th textColor={'white'}>
            Capacity
          </Th>
          <Th>

          </Th>
        </Tr>
      </Thead>
      <Tbody>
        {
          sessionList.map((session) => <SessionListItem session={session} />)
        }
      </Tbody>
    </Table>
  )
}



const SessionIndex: NextPage = () => {
  const [isHydrated, setHydrated] = useState<boolean>(false);
  useEffect(() => {
    setHydrated(true);
  }, []);


  if (!isHydrated) {
    return (<>
    </>);
  }
  return (
    <Box>
      <Navbar />
      <Center>
        <Box
          my={'0.5rem'}
          bg={"white"}
          minW={'5xl'}
          maxHeight={'calc(100vh - 64px)'}
          overflowY='auto'
        >
          <SessionList sessionList={sessionSample} />
        </Box>
      </Center>
    </Box>
  )
}

export default SessionIndex;