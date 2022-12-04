import '../styles/globals.css';
import type { AppProps } from 'next/app'
import { ChakraProvider, extendTheme, useColorMode, useColorModeValue } from '@chakra-ui/react';
import defaultComponentStyles from '../styles/defaultStyles';
import IconButton from '../styles/defaultStyles/IconButton';
const colors = {
  "red": {
    "50": "#FFE5E5",
    "100": "#FFB8B8",
    "200": "#FF8A8A",
    "300": "#FF5C5C",
    "400": "#FF2E2E",
    "500": "#FF0000",
    "600": "#CC0000",
    "700": "#990000",
    "800": "#660000",
    "900": "#330000"
  },
  "primaryFontColor": {
    lightMode: "red.50",
    darkMode: "red.50"
  },
  "secondaryFontColor": {
    lightMode: "red.50",
    darkMode: "red.50"
  }
}


const theme = extendTheme(
  defaultComponentStyles,
  {

  colors,
  styles:{
    global:{
      body:{
        fontSize: "18px",
        fontWeight: "400"
      }
    }
  }
}
);
console.log(theme);

function MyApp({ Component, pageProps }: AppProps) {

  return(
    <ChakraProvider theme={theme}>
      <Component {...pageProps} />
    </ChakraProvider> 
  )
}

export default MyApp
