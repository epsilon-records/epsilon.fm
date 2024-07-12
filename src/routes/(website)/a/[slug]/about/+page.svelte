<script>
	import skills from '../Skills';
	import { Badge } from '$lib/components/ui/badge';
	export let data;
</script>

<svelte:head>
	<title>{data.stageName} — About</title>
</svelte:head>

<div class="container">
	<h1 class="text-white">About</h1>
	<p class="bg-slate-900 p-4 text-white">{data.biography}</p>
	<br />
	{#each Object.entries(skills) as [section, technologies]}
		<div class="w-min bg-slate-900 p-2 text-white">
			{section}:
		</div>

		{#each technologies as technology}
			<Badge class="m-2">{technology}</Badge>
		{/each}
	{/each}
</div>

<style>
	.container {
		max-width: 900px;
		padding: 0;
		display: flex;
		justify-content: center;
	}

	main {
		max-width: 100%;
		min-height: 500px;
		text-align: left;
		margin: 0 auto;
		box-sizing: border-box;
	}

	h1 {
		font-weight: 700;
		margin: 0 0 50px 0;
		font-size: 36px;
		text-align: start;
	}

	h2 {
		margin-top: 50px;
	}

	.list {
		display: flex;
		flex-direction: column;
		gap: 30px;
	}

	@media (min-width: 900px) {
		.list {
			flex-direction: row;
		}
		main > h1 {
			font-size: 48px;
		}
	}
</style>
