import { ReactNode } from "react";
import { 
  Box,
  Flex,
  Avatar,
  HStack,
  Link,
  Text,
  IconButton,
  Button,
  Menu,
  MenuButton,
  MenuList,
  MenuItem,
  MenuDivider,
  useDisclosure,
  useColorModeValue,
  Stack,
  Divider,
  Spacer
} from "@chakra-ui/react";
import { HamburgerIcon, CloseIcon, EmailIcon, BellIcon } from '@chakra-ui/icons';


interface LinkType {
  name: string;
  url: string;
}

const links:LinkType[] = [
  {
    name: "Dashboard",
    url: "/dashboard"
  },
  {
    name: "Sessions",
    url: "/sessions"
  },
  {
    name: "Tutors",
    url: "/tutors"
  },
  {
    name:"Tutor Organizations",
    url: "/orgs"
  }
]

const NavLink = ({ href, children }: { href:string, children: ReactNode }) => (
  <Link
    px={2}
    py={1}
    rounded={'md'}
    _hover={{
      textDecoration: 'none',
      bg: useColorModeValue('red.700', 'red.700'),
    }}
    href={href}>
    {children}
  </Link>
);

export default function Navbar() {
  const { isOpen, onOpen, onClose } = useDisclosure();

  return (
    <>
      <Box bg={useColorModeValue('red.600', 'red.900')} px={4}>
        <Flex h={16} alignItems={'center'} justifyContent={'space-between'}>
          <IconButton
            size={'md'}
            icon={isOpen ? <CloseIcon /> : <HamburgerIcon />}
            aria-label={'Open Menu'}
            display={{ md: 'none' }}
            onClick={isOpen ? onClose : onOpen}
          />
          <HStack spacing={8} alignItems={'center'}>
            <Box>
              <Link href={'/'}>
                <Text color={useColorModeValue('white', 'white')}>
                  Tutor Tim 
                </Text>
              </Link>
            </Box>
            <HStack
              as={'nav'}
              spacing={4}
              display={{ base: 'none', md: 'flex' }}>
              {links.map((link) => (
                <NavLink key={link.name} href={link.url}>
                  <Text color={useColorModeValue('white', 'white')}>
                    {link.name}
                  </Text>
                </NavLink>
              ))}
            </HStack>
          </HStack>
          
          <HStack spacing={2} alignItems={'center'}>
              <Link href={"/inbox"}>
                <IconButton
                  size={'lg'}
                  icon={<EmailIcon />}
                  aria-label={'Messages'}
                  display={{ base: 'none', md: 'flex' }}
                  variant="solid"
                  color={useColorModeValue('white', 'white')}
                  backgroundColor={useColorModeValue('red.600', 'red.700')}
                  _hover={{
                    backgroundColor: useColorModeValue('red.700', 'red.700'),
                  }}
                />
              </Link>
              <IconButton
                size={'lg'}
                icon={<BellIcon />}
                aria-label={'Messages'}
                display={{ base: 'none', md: 'flex' }}
                onClick={() => console.log('Messages button clicked')}
                variant="solid"
                color={useColorModeValue('white', 'white')}
                backgroundColor={useColorModeValue('red.600', 'red.700')}
                _hover={{
                  backgroundColor: useColorModeValue('red.700', 'red.700'),
                }}
              />
            
            <Menu>
              <MenuButton
                as={Button}
                rounded={'full'}
                variant={'link'}
                cursor={'pointer'}
                minW={0}>
                <Avatar
                  size={'sm'}
                  name="Placeholder Name"
                />
              </MenuButton>
              <MenuList
                bgColor={useColorModeValue('red.600', 'red.900')}
              >
                {['Link 1', 'Link 2', 'Link 3'].map((link)=>{
                  return(
                    <MenuItem
                    _hover={
                      {
                        bg: useColorModeValue('red.700', 'red.700'),
                      }
                    }
                    key={link}>
                      <Text color={useColorModeValue('white', 'white')}>
                        {link}
                      </Text>
                    </MenuItem>
                  )
                })}
              </MenuList>
            </Menu>
          </HStack>
        </Flex>

        {isOpen ? (
          <Box pb={4} display={{ md: 'none' }}>
            <Stack as={'nav'} spacing={4}>
              {links.map((link) => (
                <NavLink key={link.name} href={link.url}>
                  <Text color={useColorModeValue('white', 'white')}>
                    {link.name}
                  </Text>
                </NavLink>
              ))}
            </Stack>
          </Box>
        ) : null}
      </Box>
    </>
  );
}