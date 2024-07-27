<script lang="ts">
	import GitHubCorner from './GitHubCorner.svelte';
	import * as Card from '$lib/components/ui/card';
	import { Button } from '$lib/components/ui/button/index';
	import SignedIn from 'clerk-sveltekit/client/SignedIn.svelte';
	import SignedOut from 'clerk-sveltekit/client/SignedOut.svelte';
	import SignInButton from 'clerk-sveltekit/client/SignInButton.svelte';
	import SignUpButton from 'clerk-sveltekit/client/SignUpButton.svelte';
	import Typewriter from 'svelte-typewriter';
	import { slug } from '$lib/stores/main';
	import type { PageData } from './$types.js';
	import Dashboard from '$lib/components/blocks/dashboard/dashboard.svelte';

	export let data: PageData;

	function loadConvertKit(node: HTMLElement) {
		const script = document.createElement('script');
		script.src = 'https://epsilon.ck.page/47e61bac90/index.js';
		script.async = true;
		script.setAttribute('data-uid', '47e61bac90');
		node.appendChild(script);
	}

	slug.set(data.slug);
</script>

<svelte:head>
	<title>Epsilon FM</title>
	<meta
		name="description"
		content="Our modern open-source music distribution platform includes a beautifully designed artist website, customised merch, generative AI music videos, and access to over one hundred global digital streaming platforms including Beatport, Traxsource, and Juno Download."
	/>
</svelte:head>

<section>
	<SignedIn>
		<Dashboard></Dashboard>
	</SignedIn>
	<SignedOut>
		<GitHubCorner />
		<Card.Root class="m-4">
			<Card.Header>
				<Card.Title>Epsilon FM</Card.Title>
				<Card.Description>A modern open-source music business platform.</Card.Description>
			</Card.Header>
			<Card.Content>
				<Typewriter mode="scramble" scrambleSlowdown={true} keepCursorOnFinish={true}>
					<h4 class="scroll-m-20 text-center text-4xl font-semibold tracking-tight">Welcome</h4>
				</Typewriter>
			</Card.Content>
			<Card.Content>
				<SignedOut>
					<Button class="m-2">
						<SignInButton mode="modal">Login</SignInButton>
					</Button>
					<Button class="m-2">
						<SignUpButton mode="modal">Sign up</SignUpButton>
					</Button>
				</SignedOut>
			</Card.Content>
		</Card.Root>
		<Card.Root class="m-4">
			<Card.Header>
				<div class="flex items-center justify-center">
					<p class="font-mono text-2xl">Join our Newsletter</p>
				</div>
			</Card.Header>
			<Card.Content>
				<div class="flex items-center justify-center" use:loadConvertKit>
					<!-- ConvertKit form will be inserted here by the script -->
				</div>
			</Card.Content>
		</Card.Root>
	</SignedOut>
</section>
