<svelte:head>
	{#if import.meta.env.PUBLIC_METICULOUS_RECORDING_TOKEN}
		<script
			data-project-id={import.meta.env.PUBLIC_METICULOUS_RECORDING_TOKEN}
			data-is-production-environment={import.meta.env.MODE === 'production'}
			src="https://snippet.meticulous.ai/v1/meticulous.js"
		></script>
	{/if}
	{#if import.meta.env.PUBLIC_WEGLOT_API_KEY}
		<script type="text/javascript" src="https://cdn.weglot.com/weglot.min.js"></script>
		<script>
			Weglot.initialize({
				api_key: import.meta.env.PUBLIC_WEGLOT_API_KEY
			});
		</script>
	{/if}
</svelte:head>
