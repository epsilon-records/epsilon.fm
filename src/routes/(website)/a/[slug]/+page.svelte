<script type="ts">
	import Gmail from 'svelte-simples/Gmail.svelte';
	import Instagram from 'svelte-simples/Instagram.svelte';
	import Facebook from 'svelte-simples/Facebook.svelte';
	import Soundcloud from 'svelte-simples/Soundcloud.svelte';
	import Youtube from 'svelte-simples/Youtube.svelte';
	import Tiktok from 'svelte-simples/Tiktok.svelte';
	import Bandsintown from 'svelte-simples/Bandsintown.svelte';
	import { modalOpened } from '$lib/stores/website';
	import { createQuery } from '@tanstack/svelte-query';
	import { api } from '$lib/api';
	import { error } from '@sveltejs/kit';
	export let data;

	const artist = createQuery({
		queryKey: ['artists'],
		queryFn: () => api().getArtist(data.orgId)
	});
	if (!artist) {
		error(404);
	}
</script>

<svelte:head>
	<title>{$artist.data?.stageName}</title>
</svelte:head>
<main>
	<div class="text-8xl text-white">{$artist.data?.stageName.toUpperCase()}</div>
	<div class="pt-12 text-3xl text-white">DJ & Producer</div>
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
		{#if $artist.data?.instagramProfileLink}
			<a
				href={$artist.data?.instagramProfileLink}
				aria-label="Instagram"
				target="_blank"
				rel="noopener noreferrer"
			>
				<div class="icon">
					<Instagram />
				</div>
			</a>
		{/if}
		{#if $artist.data?.facebookProfileLink}
			<a
				href={$artist.data?.facebookProfileLink}
				aria-label="Facebook"
				target="_blank"
				rel="noopener noreferrer"
			>
				<div class="icon">
					<Facebook />
				</div>
			</a>
		{/if}
		{#if $artist.data?.soundcloudProfileLink}
			<a
				href={$artist.data?.soundcloudProfileLink}
				aria-label="SoundCloud"
				target="_blank"
				rel="noopener noreferrer"
			>
				<div class="icon">
					<Soundcloud />
				</div>
			</a>
		{/if}
		{#if $artist.data?.bandsintownProfileLink}
			<a
				href={$artist.data?.bandsintownProfileLink}
				aria-label="Bandsintown"
				target="_blank"
				rel="noopener noreferrer"
			>
				<div class="icon">
					<Bandsintown />
				</div>
			</a>
		{/if}
		{#if $artist.data?.tiktokProfileLink}
			<a
				href={$artist.data?.tiktokProfileLink}
				aria-label="TikTok"
				target="_blank"
				rel="noopener noreferrer"
			>
				<div class="icon pb-4 pl-2">
					<Tiktok />
				</div>
			</a>
		{/if}
		{#if $artist.data?.youtubeChannelLink}
			<a
				href={$artist.data?.youtubeChannelLink}
				aria-label="YouTube"
				target="_blank"
				rel="noopener noreferrer"
			>
				<div class="icon">
					<Youtube />
				</div>
			</a>
		{/if}
	</div>
</main>

<style>
	a {
		color: white;
		text-decoration: none;
	}
	main {
		text-align: center;
		padding: 0;
		margin: 0 auto;
		text-align: center;

		display: flex;
		flex-direction: column;
		height: calc(100vh - 80px - 88px);
		justify-content: center;
		align-items: center;
	}

	.icons {
		display: flex !important;
		justify-content: center !important;
		align-items: center;
		gap: 20px;
		cursor: pointer;
		font-size: 30px;
		display: flex;
		justify-content: space-between;
		max-width: 200px;
		margin: 50px auto 0;
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
