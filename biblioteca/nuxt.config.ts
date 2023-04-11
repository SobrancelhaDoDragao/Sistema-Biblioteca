// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
    css:['~/assets/css/variaveis.css'],
    modules: [
      '@pinia/nuxt',
      '@nuxt/image-edge',
    ],
    image: {
      domains: ['http://localhost:8000/static/img'],
    },
    runtimeConfig: {

      public: {
        apiBase: '', // can be overridden by NUXT_PUBLIC_API_BASE environment variable
      }
    },

  })
  