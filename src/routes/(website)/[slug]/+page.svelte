<script lang="ts">
	import Gmail from 'svelte-simples/Gmail.svelte';
	// import Instagram from 'svelte-simples/Instagram.svelte';
	// import Facebook from 'svelte-simples/Facebook.svelte';
	// import Soundcloud from 'svelte-simples/Soundcloud.svelte';
	// import Youtube from 'svelte-simples/Youtube.svelte';
	// import Tiktok from 'svelte-simples/Tiktok.svelte';
	// import Bandsintown from 'svelte-simples/Bandsintown.svelte';
	import { modalOpened } from '$lib/stores/website';
	import { createQuery } from '@tanstack/svelte-query';
	import { ArtistsService } from '$lib/api/ms/client/services.gen';
	import { error } from '@sveltejs/kit';

	export let data: { org_id: string };

	const artist = createQuery({
		queryKey: ['artists', data.org_id],
		queryFn: async () => ArtistsService.endpointV1ArtistsGetIdGet
	});
	$: if ($artist.error) {
		console.log($artist.error);
		error(404);
	}
</script>

<svelte:head>
	<title>Vozz Rich</title>
	<meta name="description" content="Official page of Vozz Rich. DJ & Producer." />
</svelte:head>

<main>
	<h1 class="text-8xl text-white">VOZZ RICH</h1>
	<p class="pt-12 text-3xl text-white">DJ & Producer</p>
	<div class="icons">
		<div
			role="button"
			tabindex="0"
			on:keypress={() => {
				modalOpened.set(true);
			}}
			on:click={() => {
				modalOpened.set(true);
			}}
		>
			<div class="icon">
				<Gmail />
			</div>
		</div>
		<!-- {#if $artist.data?.instagram_profile_link}
			<a
				href={$artist.data?.instagram_profile_link}
				aria-label="Instagram"
				target="_blank"
				rel="noopener noreferrer"
			>
				<div class="icon">
					<Instagram />
				</div>
			</a>
		{/if}
		{#if $artist.data?.facebook_profile_link}
			<a
				href={$artist.data?.facebook_profile_link}
				aria-label="Facebook"
				target="_blank"
				rel="noopener noreferrer"
			>
				<div class="icon">
					<Facebook />
				</div>
			</a>
		{/if}
		{#if $artist.data?.soundcloud_profile_link}
			<a
				href={$artist.data?.soundcloud_profile_link}
				aria-label="SoundCloud"
				target="_blank"
				rel="noopener noreferrer"
			>
				<div class="icon">
					<Soundcloud />
				</div>
			</a>
		{/if}
		{#if $artist.data?.bandsintown_profile_link}
			<a
				href={$artist.data?.bandsintown_profile_link}
				aria-label="Bandsintown"
				target="_blank"
				rel="noopener noreferrer"
			>
				<div class="icon">
					<Bandsintown />
				</div>
			</a>
		{/if}
		{#if $artist.data?.tiktok_profile_link}
			<a
				href={$artist.data?.tiktok_profile_link}
				aria-label="TikTok"
				target="_blank"
				rel="noopener noreferrer"
			>
				<div class="icon pb-4 pl-2">
					<Tiktok />
				</div>
			</a>
		{/if}
		{#if $artist.data?.youtube_channel_link}
			<a
				href={$artist.data?.youtube_channel_link}
				aria-label="YouTube"
				target="_blank"
				rel="noopener noreferrer"
			>
				<div class="icon">
					<Youtube />
				</div>
			</a>
		{/if} -->
	</div>
</main>

<style>
	:root {
		--text-color: white;
	}

	/* a {
		color: var(--text-color);
		text-decoration: none;
	} */

	main {
		display: flex;
		flex-direction: column;
		height: calc(100vh - 80px - 88px);
		justify-content: center;
		align-items: center;
		text-align: center;
		padding: 0;
		margin: 0 auto;
	}

	.icons {
		display: flex;
		justify-content: center;
		align-items: center;
		gap: 20px;
		margin: 50px auto 0;
		max-width: 200px;
	}

	.icon {
		cursor: pointer;
		transition: color 0.2s ease-in-out;
		width: 40px;
	}

	@media (min-width: 600px) {
		main {
			max-width: none;
		}
	}
</style>
