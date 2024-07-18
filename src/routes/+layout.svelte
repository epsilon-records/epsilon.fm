<script lang="ts">
	import { METICULOUS_RECORDING_TOKEN, WEGLOT_API_KEY } from '$env/static/private';
</script>

<svelte:head>
	<script
		data-project-id={METICULOUS_RECORDING_TOKEN}
		data-is-production-environment={import.meta.env.MODE === 'production'}
		src="https://snippet.meticulous.ai/v1/meticulous.js"
	></script>
	<script type="text/javascript" src="https://cdn.weglot.com/weglot.min.js"></script>
	<script>
		Weglot.initialize({
			api_key: WEGLOT_API_KEY
		});
	</script>
</svelte:head>
