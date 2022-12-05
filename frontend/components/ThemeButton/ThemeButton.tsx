import * as React from 'react';
import { useState, useEffect } from 'react';
import { Button, ButtonProps } from '@chakra-ui/react';












interface ThemeButtonProps {
  children?: React.ReactNode;
}

export default ({children, ...props}:ThemeButtonProps & ButtonProps) => {
  return( 
  <Button 
    backgroundColor={'red.600'}
    textColor={'white'}
    _hover={{
      backgroundColor:'red.700'
    }}
    _pressed={{
      backgroundColor: 'red.800'
    }}
    {...props}
  >
    {children}
  </Button>
  )
}





