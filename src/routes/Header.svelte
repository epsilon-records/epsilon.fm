<script>
	import { page } from '$app/stores';
	import logo from '$lib/images/acid-logo.png';
	import github from '$lib/images/github.svg';
	import UserButton from 'clerk-sveltekit/client/UserButton.svelte';
	import SignedIn from 'clerk-sveltekit/client/SignedIn.svelte';
	import SignedOut from 'clerk-sveltekit/client/SignedOut.svelte';
</script>

<header>
	<div class="corner m-8">
		<a href="https://epsilon.fm">
			<img src={logo} alt="Epsilon Distribution" />
		</a>
	</div>
	<nav class="m-8">
		<svg viewBox="0 0 2 3" aria-hidden="true">
			<path d="M0,0 L1,2 C1.5,3 1.5,3 2,3 L2,0 Z" />
		</svg>
		<ul>
			<li aria-current={$page.url.pathname === '/' ? 'page' : undefined}>
				<a href="/">Home</a>
			</li>
			<li aria-current={$page.url.pathname === '/faq' ? 'page' : undefined}>
				<a href="/">FAQ</a>
			</li>
			<li aria-current={$page.url.pathname === '/profile' ? 'page' : undefined}>
				<a href="/profile">Profile</a>
			</li>
			<li aria-current={$page.url.pathname === '/releases' ? 'page' : undefined}>
				<a href="/">Releases</a>
			</li>
			<li aria-current={$page.url.pathname === '/merch' ? 'page' : undefined}>
				<a href="/">Merch</a>
			</li>
			<li aria-current={$page.url.pathname === '/website' ? 'page' : undefined}>
				<a href="/">Website</a>
			</li>
			<li aria-current={$page.url.pathname === '/social' ? 'page' : undefined}>
				<a href="/">Social</a>
			</li>
			<li aria-current={$page.url.pathname === '/admin' ? 'page' : undefined}>
				<a href="/">Admin</a>
			</li>
			<li aria-current={$page.url.pathname === '/settings' ? 'page' : undefined}>
				<a href="/">Settings</a>
			</li>
		</ul>
		<svg viewBox="0 0 2 3" aria-hidden="true">
			<path d="M0,0 L0,3 C0.5,3 0.5,3 1,2 L2,0 Z" />
		</svg>
	</nav>
	<div class="corner m-8">
		<SignedIn>
			<UserButton afterSignOutUrl="/" />
		</SignedIn>
		<SignedOut>
			<a href="https://github.com/natehouk/epsilon.fm">
				<img src={github} alt="GitHub" />
			</a>
		</SignedOut>
	</div>
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
