import { defineStyleConfig } from "@chakra-ui/styled-system";


export default defineStyleConfig({
  baseStyle: {
    borderRadius: "50%",
    padding: "0.5rem",
    backgroundColor: "red.500",
    color: "red.50",
  },
  sizes: {
    sm: {
      width: "1.5rem",
      height: "1.5rem",
    },
    md: {
      width: "2rem",
      height: "2rem",
    },
    lg: {
      width: "2.5rem",
      height: "2.5rem",
    },
  },
  variants: {
    solid: {
      backgroundColor: "red.500",
      color: "red.50",
      
    },
    outline: {
      backgroundColor: "red.50",
      color: "red.500",
      border: "1px solid",
      borderColor: "red.500",
    },
  },
  defaultProps: {
    size: "md",
    variant: "solid",
  },
});
