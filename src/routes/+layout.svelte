<script>
	import {
		PUBLIC_MODE,
		PUBLIC_WEGLOT_API_KEY,
		PUBLIC_METICULOUS_RECORDING_TOKEN
	} from '$env/static/public';
</script>

<svelte:head>
	{#if PUBLIC_METICULOUS_RECORDING_TOKEN}
		<script
			data-project-id={PUBLIC_METICULOUS_RECORDING_TOKEN}
			data-is-production-environment={PUBLIC_MODE === 'production'}
			src="https://snippet.meticulous.ai/v1/meticulous.js"
		></script>
	{/if}
	{#if PUBLIC_WEGLOT_API_KEY}
		<script type="text/javascript" src="https://cdn.weglot.com/weglot.min.js"></script>
		<script>
			Weglot.initialize({
				api_key: 'wg_0a000660678e1bd22f8ae33745094d231'
			});
		</script>
	{/if}
</svelte:head>
<slot />
