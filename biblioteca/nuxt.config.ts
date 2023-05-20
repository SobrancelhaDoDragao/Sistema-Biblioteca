// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
    css:['~/assets/css/padrao.css'],
    modules: [
      '@pinia/nuxt',
      '@nuxt/image-edge',
    ],
    image: {
      domains: [
        // Só funciona assim, tem que mostrar os dominios permitidos 
        '127.0.0.1:8000','localhost:8000','192.168.1.12:8000'
      ],
    },
    runtimeConfig: {

      public: {
        apiBase: process.env.NUXT_PUBLIC_API_BASE || 'http://127.0.0.1:8000/'
      }
    },

  })
       