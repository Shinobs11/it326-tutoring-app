import * as React from 'react';
import { useState, useEffect } from 'react';
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

interface ProfilePropsType{
  firstName: string;
  lastName: string;
  emailAddress: string;
  phoneNumber: string;
}

const Profile = ({firstName, lastName, emailAddress, phoneNumber,...props}: ProfilePropsType) =>{


  return(
    <Container>
      <HStack>
        <Text>First Name: </Text>
        <Text>{firstName}</Text>
      </HStack>
      <HStack>
        <Text>Last Name: </Text>
        <Text>{lastName}</Text>
      </HStack>
      <HStack>
        <Text>Email Address: </Text>
        <Text>{emailAddress}</Text>
      </HStack>
      <HStack>
        <Text>Phone Number: </Text>
        <Text>{phoneNumber}</Text> 
      </HStack>     
    </Container>
  )

}

export default Profile;