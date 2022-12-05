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
  "gray": {
    "50": "#F2F2F2",
    "100": "#DBDBDB",
    "200": "#C4C4C4",
    "300": "#ADADAD",
    "400": "#969696",
    "500": "#808080",
    "600": "#666666",
    "700": "#4D4D4D",
    "800": "#333333",
    "900": "#1A1A1A"
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
        fontWeight: "400",
        backgroundColor: 'gray.50'
      }
    }
  },
  components:{
    Button: {
      backgroundColor: 'red.600',
      textColor: 'white'
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
