<script lang="ts">
	import * as Card from '$lib/components/ui/card';
	import { Button } from '$lib/components/ui/button/index';
	import SignedIn from 'clerk-sveltekit/client/SignedIn.svelte';
	import SignedOut from 'clerk-sveltekit/client/SignedOut.svelte';
	import SignInButton from 'clerk-sveltekit/client/SignInButton.svelte';
	import SignUpButton from 'clerk-sveltekit/client/SignUpButton.svelte';
	import partners from '$lib/images/partners.png';
	import Typewriter from 'svelte-typewriter';
	import Header from './Header.svelte';
	import { createUploader } from '$lib/utils/uploadthing';
	import { UploadDropzone } from '@uploadthing/svelte';
	import { slug } from '$lib/stores/main';
	import type { PageData } from './$types.js';
	export let data: PageData;
	const uploader = createUploader('imageUploader', {
		onClientUploadComplete: (res) => {
			console.log(`onClientUploadComplete`, res);
			alert('Upload Completed');
		},
		onUploadError: (error: Error) => {
			alert(`ERROR! ${error.message}`);
		}
	});

	slug.set(data.slug);
</script>

<svelte:head>
	<title>Epsilon Distribution</title>
	<meta
		name="description"
		content="Our modern open-source music distribution platform includes features like an artist website, social media management, and merch, empowering you with global reach and full control over your creative work."
	/>
</svelte:head>

<section>
	<SignedIn>
		<UploadDropzone {uploader} />
	</SignedIn>
	<SignedOut>
		<Card.Root class="m-4">
			<Card.Header>
				<Card.Title>EpsilonFM</Card.Title>
				<Card.Description>A modern open-source music business platform.</Card.Description>
			</Card.Header>
			<Card.Content>
				<Typewriter>
					<h4 class="scroll-m-20 text-center text-4xl font-semibold tracking-tight">
						Unlimited music distribution for just $29/month
					</h4>
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
					<p class="font-mono text-2xl">Goodbye DistroKid. Hello Epsilon.</p>
				</div></Card.Header
			>
			<Card.Content>
				<p class="font-mono">
					🎉 Discover our modern open-source platform, meticulously designed with your needs in
					mind. We offer a comprehensive suite of features that empower you to take control of your
					creative journey. 🎨 Whether you're an emerging artist or an established performer, our
					tools are tailored to help you thrive in the digital age. 🌟 With capabilities such as
					creating a professional artist website 🌐, managing social media 📱, and offering
					merchandise options 🛍️, you can expand your global reach and fully manage your artistic
					presence. 🌍✨
				</p>
			</Card.Content>
		</Card.Root>
		<Card.Root class="m-4">
			<Card.Header>
				<div class="flex items-center justify-center">
					<p class="font-mono text-2xl">Industry Partners</p>
				</div></Card.Header
			>
			<Card.Content>
				<p class="font-mono">
					We believe in the power of collaboration. That’s why we partner with leading companies in
					the music industry to bring you unparalleled opportunities and experiences. Our extensive
					network ensures you have access to the best resources and support available. From
					distribution to promotion, we provide everything you need to succeed. Our platform makes
					it easy to get your music on all major streaming platforms and digital stores, ensuring
					your tracks are available to listeners everywhere.
				</p>
			</Card.Content>
			<Card.Content>
				<img alt="Epsilon Distribution Partners" src={partners} />
			</Card.Content>
		</Card.Root>
		<Card.Root class="m-4">
			<Card.Header>
				<div class="flex items-center justify-center">
					<p class="font-mono text-2xl">Join our Newsletter</p>
				</div>
			</Card.Header>
			<Card.Content>
				<div class="flex items-center justify-center">
					<script
						async
						data-uid="47e61bac90"
						src="https://epsilon.ck.page/47e61bac90/index.js"
					></script>
				</div>
			</Card.Content>
		</Card.Root>
	</SignedOut>
</section>
