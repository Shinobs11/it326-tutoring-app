/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  swcMinify: true,
  output: 'standalone' //https://github.com/vercel/next.js/tree/canary/examples/with-docker
}

module.exports = nextConfig
