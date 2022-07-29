import { defineConfig } from 'vite'
import { svelte } from '@sveltejs/vite-plugin-svelte'

// https://vitejs.dev/config/
export default defineConfig({
	base: "/yellowbelt-canadian-cities-2022",
	plugins: [svelte()]
})
