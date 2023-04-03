// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
    css:['~/assets/variaveis.css'],
    modules: [
      '@pinia/nuxt',
    ],
    runtimeConfig: {

      public: {
        apiBase: '', // can be overridden by NUXT_PUBLIC_API_BASE environment variable
      }
    },

  })
  