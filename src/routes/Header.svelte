<script>
	import { page } from '$app/stores';
	import logo from '$lib/images/acid-logo.png';
	import github from '$lib/images/github.svg';
	import UserButton from 'clerk-sveltekit/client/UserButton.svelte';
	import SignedIn from 'clerk-sveltekit/client/SignedIn.svelte';
	import SignedOut from 'clerk-sveltekit/client/SignedOut.svelte';
	import { Navbar, NavBrand, NavLi, NavUl, NavHamburger, Button, Input } from 'flowbite-svelte';
	import * as Menubar from '$lib/components/ui/menubar';

	let bookmarks = false;
	let fullUrls = true;

	const profileRadioValue = 'benoit';
</script>

<header>
	<Navbar class="m-4">
		<NavBrand href="/">
			<img src={logo} class="me-3 h-9 sm:h-9" alt="Epsilon Distribution" />
		</NavBrand>
		<div class="flex md:order-2">
			<div class="corner">
				<SignedIn>
					<UserButton afterSignOutUrl="/" />
				</SignedIn>
				<SignedOut>
					<a href="https://github.com/natehouk/epsilon.fm">
						<img src={github} alt="GitHub" />
					</a>
				</SignedOut>
			</div>
			<NavHamburger />
		</div>
		<NavUl class="order-1">
			<NavLi href="/" active={true}>Home</NavLi>
			<NavLi href="/">FAQ</NavLi>
			<NavLi href="/profile">Profile</NavLi>
			<NavLi href="/">Releases</NavLi>
			<NavLi href="/">Merch</NavLi>
			<NavLi href="/">Website</NavLi>
			<NavLi href="/">Social</NavLi>
			<NavLi href="/">Royalties</NavLi>
			<NavLi href="/">Admin</NavLi>
			<NavLi href="/">Settings</NavLi>
		</NavUl>
	</Navbar>
</header>

<style>
	header {
		display: flex;
		justify-content: space-between;
	}

	.corner {
		width: 3em;
		height: 3em;
	}

	.corner a {
		display: flex;
		align-items: center;
		justify-content: center;
		width: 100%;
		height: 100%;
	}

	.corner img {
		width: 2em;
		height: 2em;
		object-fit: contain;
	}

	nav {
		display: flex;
		justify-content: center;
		--background: rgba(255, 255, 255, 0.7);
	}

	svg {
		width: 2em;
		height: 3em;
		display: block;
	}

	path {
		fill: var(--background);
	}

	ul {
		position: relative;
		padding: 0;
		margin: 0;
		height: 3em;
		display: flex;
		justify-content: center;
		align-items: center;
		list-style: none;
		background: var(--background);
		background-size: contain;
	}

	li {
		position: relative;
		height: 100%;
	}

	li[aria-current='page']::before {
		--size: 6px;
		content: '';
		width: 0;
		height: 0;
		position: absolute;
		top: 0;
		left: calc(50% - var(--size));
		border: var(--size) solid transparent;
		border-top: var(--size) solid var(--color-theme-1);
	}

	nav a {
		display: flex;
		height: 100%;
		align-items: center;
		padding: 0 0.5rem;
		color: var(--color-text);
		font-weight: 700;
		font-size: 0.8rem;
		text-transform: uppercase;
		letter-spacing: 0.1em;
		text-decoration: none;
		transition: color 0.2s linear;
	}

	a:hover {
		color: var(--color-theme-1);
	}
</style>
