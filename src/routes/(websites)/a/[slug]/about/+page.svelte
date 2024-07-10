<script>
	import skills from '$lib/Skills';
	import { page } from '$app/stores';
	/** @type {import('./$types').PageData} */
	export let data;

	$: stageName = data.stageName;
	$: biography = data.biography;
</script>

<svelte:head>
	<title>{stageName} — About</title>
</svelte:head>

<main>
	<h1>About</h1>
	<p>
		{biography}
	</p>
	<h2>Skills</h2>
	{#each Object.entries(skills) as [section, technologies]}
		<ul>
			<li>
				<h4>
					{section}:
				</h4>
				<div class="list">
					{#each technologies as technology}
						<div>
							{technology}
						</div>
					{/each}
				</div>
			</li>
		</ul>
	{/each}
</main>

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
