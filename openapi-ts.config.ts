import { defineConfig } from '@hey-api/openapi-ts';

export default defineConfig({
	client: '@hey-api/client-fetch',
	input: 'response.json',
	output: {
		lint: 'biome',
		format: 'biome',
		path: 'src/api/soundcharts/client'
	},
	types: {
		enums: 'javascript',
		dates: 'types+transform'
	},
	schemas: {
		type: 'form'
	},
	services: {
		asClass: true
	}
});
