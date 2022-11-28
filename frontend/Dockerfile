# Install dependencies only when needed
FROM node:16-alpine AS deps
# Check https://github.com/nodejs/docker-node/tree/b4117f9333da4138b03a546ec926ef50a31506c3#nodealpine to understand why libc6-compat might be needed.
# RUN apk add --no-cache libc6-compat
RUN mkdir -p /src
WORKDIR /src
ENV NODE_ENV development

# Install dependencies based on the preferred package manager
COPY package*.json /src
RUN yarn install

FROM deps AS entry
COPY docker-entrypoint.sh /src/docker-entrypoint.sh




EXPOSE 3000
ENV PORT 3000

RUN ["chmod", "+x" ,"./docker-entrypoint.sh"]
ENTRYPOINT ["./docker-entrypoint.sh"]

