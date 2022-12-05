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
import {TutorOrganization} from '../../classes';
import { tutorOrganizationSample } from '../../sampleData/tutorOrganizationSample';
import {ArrowRightIcon} from '@chakra-ui/icons'
interface TutorOrganizationListItemProps {
  tutorOrganization: TutorOrganization
}
interface TutorOrganizationListProps {
  tutorOrganizationList: TutorOrganization[]
}



const TutorOrganizationListItem: React.FunctionComponent<TutorOrganizationListItemProps> = ({ tutorOrganization, ...props }: TutorOrganizationListItemProps) => {
  const router = useRouter();
  return (
        <Tr
          _hover={{
            bg: 'gray.100'
          }}
        >
          <Td>
            {tutorOrganization.name}
          </Td>
          <Td>
            {tutorOrganization.tutors.length}
          </Td>
          <Td>
            {tutorOrganization.managers.length}
          </Td>
          <Td>
          </Td>
        </Tr>
  )
}

const TutorOrganizationList: React.FunctionComponent<TutorOrganizationListProps> = ({ tutorOrganizationList, ...props }: TutorOrganizationListProps) => {
  return (
    <Table>
      <Thead zIndex={1} top={0} position={'sticky'} bg='red.600'>
        <Tr>
          <Td textColor='white'>
            Name
          </Td>
          <Td textColor='white' >
            # of tutors
          </Td>
          <Td textColor='white'>
            # of managers
          </Td>
          <Td textColor='white'>
            # of sessions(PLACEHOLDER)
          </Td>
        </Tr>
      </Thead>
      <Tbody>
        {
          tutorOrganizationList.map((tutorOrganization) => <TutorOrganizationListItem tutorOrganization={tutorOrganization} />)
        }
      </Tbody>
    </Table>
  )
}



const TutorOrganizationIndex: NextPage = () => {
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
          
          <TutorOrganizationList tutorOrganizationList={tutorOrganizationSample} />
        </Box>
      </Center>
    </Box>
  )
}

export default TutorOrganizationIndex;