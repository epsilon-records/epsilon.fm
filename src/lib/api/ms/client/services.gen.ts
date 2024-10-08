// This file is auto-generated by @hey-api/openapi-ts

import {
	createClient,
	createConfig,
	type Options,
	urlSearchParamsBodySerializer
} from '@hey-api/client-fetch';
import type {
	LoginForAccessTokenV1SystemAuthLoginPostData,
	LoginForAccessTokenV1SystemAuthLoginPostError,
	LoginForAccessTokenV1SystemAuthLoginPostResponse,
	RefreshAccessTokenV1SystemAuthRefreshPostError,
	RefreshAccessTokenV1SystemAuthRefreshPostResponse,
	LogoutV1SystemAuthLogoutPostError,
	LogoutV1SystemAuthLogoutPostResponse,
	EndpointV1ArtistsPostData,
	EndpointV1ArtistsPostError,
	EndpointV1ArtistsPostResponse,
	EndpointV1ArtistsGetData,
	EndpointV1ArtistsGetError,
	EndpointV1ArtistsGetResponse,
	ReadArtistV1ArtistsOrgIdGetData,
	ReadArtistV1ArtistsOrgIdGetError,
	ReadArtistV1ArtistsOrgIdGetResponse,
	EndpointV1ArtistsOrgIdIdGetData,
	EndpointV1ArtistsOrgIdIdGetError,
	EndpointV1ArtistsOrgIdIdGetResponse,
	EndpointV1ArtistsOrgIdIdPatchData,
	EndpointV1ArtistsOrgIdIdPatchError,
	EndpointV1ArtistsOrgIdIdPatchResponse,
	EndpointV1ArtistsOrgIdIdDeleteData,
	EndpointV1ArtistsOrgIdIdDeleteError,
	EndpointV1ArtistsOrgIdIdDeleteResponse,
	EndpointV1TracksPostData,
	EndpointV1TracksPostError,
	EndpointV1TracksPostResponse,
	EndpointV1TracksGetData,
	EndpointV1TracksGetError,
	EndpointV1TracksGetResponse,
	EndpointV1TracksIdGetData,
	EndpointV1TracksIdGetError,
	EndpointV1TracksIdGetResponse,
	EndpointV1TracksIdPatchData,
	EndpointV1TracksIdPatchError,
	EndpointV1TracksIdPatchResponse,
	EndpointV1TracksIdDeleteData,
	EndpointV1TracksIdDeleteError,
	EndpointV1TracksIdDeleteResponse,
	EndpointV1GenresPostData,
	EndpointV1GenresPostError,
	EndpointV1GenresPostResponse,
	EndpointV1GenresGetData,
	EndpointV1GenresGetError,
	EndpointV1GenresGetResponse,
	EndpointV1GenresIdGetData,
	EndpointV1GenresIdGetError,
	EndpointV1GenresIdGetResponse,
	EndpointV1GenresIdPatchData,
	EndpointV1GenresIdPatchError,
	EndpointV1GenresIdPatchResponse,
	EndpointV1GenresIdDeleteData,
	EndpointV1GenresIdDeleteError,
	EndpointV1GenresIdDeleteResponse,
	EndpointV1SubgenresPostData,
	EndpointV1SubgenresPostError,
	EndpointV1SubgenresPostResponse,
	EndpointV1SubgenresGetData,
	EndpointV1SubgenresGetError,
	EndpointV1SubgenresGetResponse,
	EndpointV1SubgenresIdGetData,
	EndpointV1SubgenresIdGetError,
	EndpointV1SubgenresIdGetResponse,
	EndpointV1SubgenresIdPatchData,
	EndpointV1SubgenresIdPatchError,
	EndpointV1SubgenresIdPatchResponse,
	EndpointV1SubgenresIdDeleteData,
	EndpointV1SubgenresIdDeleteError,
	EndpointV1SubgenresIdDeleteResponse,
	EndpointV1ReleasesPostData,
	EndpointV1ReleasesPostError,
	EndpointV1ReleasesPostResponse,
	EndpointV1ReleasesGetData,
	EndpointV1ReleasesGetError,
	EndpointV1ReleasesGetResponse,
	EndpointV1ReleasesIdGetData,
	EndpointV1ReleasesIdGetError,
	EndpointV1ReleasesIdGetResponse,
	EndpointV1ReleasesIdPatchData,
	EndpointV1ReleasesIdPatchError,
	EndpointV1ReleasesIdPatchResponse,
	EndpointV1ReleasesIdDeleteData,
	EndpointV1ReleasesIdDeleteError,
	EndpointV1ReleasesIdDeleteResponse,
	EndpointV1LabelsPostData,
	EndpointV1LabelsPostError,
	EndpointV1LabelsPostResponse,
	EndpointV1LabelsGetData,
	EndpointV1LabelsGetError,
	EndpointV1LabelsGetResponse,
	EndpointV1LabelsIdGetData,
	EndpointV1LabelsIdGetError,
	EndpointV1LabelsIdGetResponse,
	EndpointV1LabelsIdPatchData,
	EndpointV1LabelsIdPatchError,
	EndpointV1LabelsIdPatchResponse,
	EndpointV1LabelsIdDeleteData,
	EndpointV1LabelsIdDeleteError,
	EndpointV1LabelsIdDeleteResponse
} from './types.gen';

export const client = createClient(createConfig());

export class AuthenticationService {
	/**
	 * Login For Access Token
	 */
	public static loginForAccessTokenV1SystemAuthLoginPost<ThrowOnError extends boolean = false>(
		options: Options<LoginForAccessTokenV1SystemAuthLoginPostData, ThrowOnError>
	) {
		return (options?.client ?? client).post<
			ThrowOnError,
			LoginForAccessTokenV1SystemAuthLoginPostResponse,
			LoginForAccessTokenV1SystemAuthLoginPostError
		>({
			...options,
			...urlSearchParamsBodySerializer,
			headers: {
				'Content-Type': 'application/x-www-form-urlencoded'
			},
			url: '/v1/system/auth/login'
		});
	}

	/**
	 * Refresh Access Token
	 */
	public static refreshAccessTokenV1SystemAuthRefreshPost<ThrowOnError extends boolean = false>(
		options?: Options<unknown, ThrowOnError>
	) {
		return (options?.client ?? client).post<
			ThrowOnError,
			RefreshAccessTokenV1SystemAuthRefreshPostResponse,
			RefreshAccessTokenV1SystemAuthRefreshPostError
		>({
			...options,
			url: '/v1/system/auth/refresh'
		});
	}

	/**
	 * Logout
	 */
	public static logoutV1SystemAuthLogoutPost<ThrowOnError extends boolean = false>(
		options?: Options<unknown, ThrowOnError>
	) {
		return (options?.client ?? client).post<
			ThrowOnError,
			LogoutV1SystemAuthLogoutPostResponse,
			LogoutV1SystemAuthLogoutPostError
		>({
			...options,
			url: '/v1/system/auth/logout'
		});
	}
}

export class ArtistsService {
	/**
	 * Endpoint
	 * Create a new Artist row in the database.
	 */
	public static endpointV1ArtistsPost<ThrowOnError extends boolean = false>(
		options: Options<EndpointV1ArtistsPostData, ThrowOnError>
	) {
		return (options?.client ?? client).post<
			ThrowOnError,
			EndpointV1ArtistsPostResponse,
			EndpointV1ArtistsPostError
		>({
			...options,
			url: '/v1/artists'
		});
	}

	/**
	 * Endpoint
	 * Read multiple Artist rows from the database with a limit and an offset.
	 */
	public static endpointV1ArtistsGet<ThrowOnError extends boolean = false>(
		options?: Options<EndpointV1ArtistsGetData, ThrowOnError>
	) {
		return (options?.client ?? client).get<
			ThrowOnError,
			EndpointV1ArtistsGetResponse,
			EndpointV1ArtistsGetError
		>({
			...options,
			url: '/v1/artists'
		});
	}

	/**
	 * Read Artist
	 */
	public static readArtistV1ArtistsOrgIdGet<ThrowOnError extends boolean = false>(
		options: Options<ReadArtistV1ArtistsOrgIdGetData, ThrowOnError>
	) {
		return (options?.client ?? client).get<
			ThrowOnError,
			ReadArtistV1ArtistsOrgIdGetResponse,
			ReadArtistV1ArtistsOrgIdGetError
		>({
			...options,
			url: '/v1/artists/{org_id}'
		});
	}

	/**
	 * Endpoint
	 * Read a single Artist row from the database by its primary keys: ['org_id', 'id'].
	 */
	public static endpointV1ArtistsOrgIdIdGet<ThrowOnError extends boolean = false>(
		options: Options<EndpointV1ArtistsOrgIdIdGetData, ThrowOnError>
	) {
		return (options?.client ?? client).get<
			ThrowOnError,
			EndpointV1ArtistsOrgIdIdGetResponse,
			EndpointV1ArtistsOrgIdIdGetError
		>({
			...options,
			url: '/v1/artists/{org_id}/{id}'
		});
	}

	/**
	 * Endpoint
	 * Update an existing Artist row in the database by its primary keys: ['org_id', 'id'].
	 */
	public static endpointV1ArtistsOrgIdIdPatch<ThrowOnError extends boolean = false>(
		options: Options<EndpointV1ArtistsOrgIdIdPatchData, ThrowOnError>
	) {
		return (options?.client ?? client).patch<
			ThrowOnError,
			EndpointV1ArtistsOrgIdIdPatchResponse,
			EndpointV1ArtistsOrgIdIdPatchError
		>({
			...options,
			url: '/v1/artists/{org_id}/{id}'
		});
	}

	/**
	 * Endpoint
	 * Soft delete a Artist row from the database by its primary keys: ['org_id', 'id'].
	 */
	public static endpointV1ArtistsOrgIdIdDelete<ThrowOnError extends boolean = false>(
		options: Options<EndpointV1ArtistsOrgIdIdDeleteData, ThrowOnError>
	) {
		return (options?.client ?? client).delete<
			ThrowOnError,
			EndpointV1ArtistsOrgIdIdDeleteResponse,
			EndpointV1ArtistsOrgIdIdDeleteError
		>({
			...options,
			url: '/v1/artists/{org_id}/{id}'
		});
	}
}

export class TracksService {
	/**
	 * Endpoint
	 * Create a new Track row in the database.
	 */
	public static endpointV1TracksPost<ThrowOnError extends boolean = false>(
		options: Options<EndpointV1TracksPostData, ThrowOnError>
	) {
		return (options?.client ?? client).post<
			ThrowOnError,
			EndpointV1TracksPostResponse,
			EndpointV1TracksPostError
		>({
			...options,
			url: '/v1/tracks'
		});
	}

	/**
	 * Endpoint
	 * Read multiple Track rows from the database with a limit and an offset.
	 */
	public static endpointV1TracksGet<ThrowOnError extends boolean = false>(
		options?: Options<EndpointV1TracksGetData, ThrowOnError>
	) {
		return (options?.client ?? client).get<
			ThrowOnError,
			EndpointV1TracksGetResponse,
			EndpointV1TracksGetError
		>({
			...options,
			url: '/v1/tracks'
		});
	}

	/**
	 * Endpoint
	 * Read a single Track row from the database by its primary keys: ['id'].
	 */
	public static endpointV1TracksIdGet<ThrowOnError extends boolean = false>(
		options: Options<EndpointV1TracksIdGetData, ThrowOnError>
	) {
		return (options?.client ?? client).get<
			ThrowOnError,
			EndpointV1TracksIdGetResponse,
			EndpointV1TracksIdGetError
		>({
			...options,
			url: '/v1/tracks/{id}'
		});
	}

	/**
	 * Endpoint
	 * Update an existing Track row in the database by its primary keys: ['id'].
	 */
	public static endpointV1TracksIdPatch<ThrowOnError extends boolean = false>(
		options: Options<EndpointV1TracksIdPatchData, ThrowOnError>
	) {
		return (options?.client ?? client).patch<
			ThrowOnError,
			EndpointV1TracksIdPatchResponse,
			EndpointV1TracksIdPatchError
		>({
			...options,
			url: '/v1/tracks/{id}'
		});
	}

	/**
	 * Endpoint
	 * Soft delete a Track row from the database by its primary keys: ['id'].
	 */
	public static endpointV1TracksIdDelete<ThrowOnError extends boolean = false>(
		options: Options<EndpointV1TracksIdDeleteData, ThrowOnError>
	) {
		return (options?.client ?? client).delete<
			ThrowOnError,
			EndpointV1TracksIdDeleteResponse,
			EndpointV1TracksIdDeleteError
		>({
			...options,
			url: '/v1/tracks/{id}'
		});
	}
}

export class GenresService {
	/**
	 * Endpoint
	 * Create a new Genre row in the database.
	 */
	public static endpointV1GenresPost<ThrowOnError extends boolean = false>(
		options: Options<EndpointV1GenresPostData, ThrowOnError>
	) {
		return (options?.client ?? client).post<
			ThrowOnError,
			EndpointV1GenresPostResponse,
			EndpointV1GenresPostError
		>({
			...options,
			url: '/v1/genres'
		});
	}

	/**
	 * Endpoint
	 * Read multiple Genre rows from the database with a limit and an offset.
	 */
	public static endpointV1GenresGet<ThrowOnError extends boolean = false>(
		options?: Options<EndpointV1GenresGetData, ThrowOnError>
	) {
		return (options?.client ?? client).get<
			ThrowOnError,
			EndpointV1GenresGetResponse,
			EndpointV1GenresGetError
		>({
			...options,
			url: '/v1/genres'
		});
	}

	/**
	 * Endpoint
	 * Read a single Genre row from the database by its primary keys: ['id'].
	 */
	public static endpointV1GenresIdGet<ThrowOnError extends boolean = false>(
		options: Options<EndpointV1GenresIdGetData, ThrowOnError>
	) {
		return (options?.client ?? client).get<
			ThrowOnError,
			EndpointV1GenresIdGetResponse,
			EndpointV1GenresIdGetError
		>({
			...options,
			url: '/v1/genres/{id}'
		});
	}

	/**
	 * Endpoint
	 * Update an existing Genre row in the database by its primary keys: ['id'].
	 */
	public static endpointV1GenresIdPatch<ThrowOnError extends boolean = false>(
		options: Options<EndpointV1GenresIdPatchData, ThrowOnError>
	) {
		return (options?.client ?? client).patch<
			ThrowOnError,
			EndpointV1GenresIdPatchResponse,
			EndpointV1GenresIdPatchError
		>({
			...options,
			url: '/v1/genres/{id}'
		});
	}

	/**
	 * Endpoint
	 * Soft delete a Genre row from the database by its primary keys: ['id'].
	 */
	public static endpointV1GenresIdDelete<ThrowOnError extends boolean = false>(
		options: Options<EndpointV1GenresIdDeleteData, ThrowOnError>
	) {
		return (options?.client ?? client).delete<
			ThrowOnError,
			EndpointV1GenresIdDeleteResponse,
			EndpointV1GenresIdDeleteError
		>({
			...options,
			url: '/v1/genres/{id}'
		});
	}
}

export class SubgenresService {
	/**
	 * Endpoint
	 * Create a new Subgenre row in the database.
	 */
	public static endpointV1SubgenresPost<ThrowOnError extends boolean = false>(
		options: Options<EndpointV1SubgenresPostData, ThrowOnError>
	) {
		return (options?.client ?? client).post<
			ThrowOnError,
			EndpointV1SubgenresPostResponse,
			EndpointV1SubgenresPostError
		>({
			...options,
			url: '/v1/subgenres'
		});
	}

	/**
	 * Endpoint
	 * Read multiple Subgenre rows from the database with a limit and an offset.
	 */
	public static endpointV1SubgenresGet<ThrowOnError extends boolean = false>(
		options?: Options<EndpointV1SubgenresGetData, ThrowOnError>
	) {
		return (options?.client ?? client).get<
			ThrowOnError,
			EndpointV1SubgenresGetResponse,
			EndpointV1SubgenresGetError
		>({
			...options,
			url: '/v1/subgenres'
		});
	}

	/**
	 * Endpoint
	 * Read a single Subgenre row from the database by its primary keys: ['id'].
	 */
	public static endpointV1SubgenresIdGet<ThrowOnError extends boolean = false>(
		options: Options<EndpointV1SubgenresIdGetData, ThrowOnError>
	) {
		return (options?.client ?? client).get<
			ThrowOnError,
			EndpointV1SubgenresIdGetResponse,
			EndpointV1SubgenresIdGetError
		>({
			...options,
			url: '/v1/subgenres/{id}'
		});
	}

	/**
	 * Endpoint
	 * Update an existing Subgenre row in the database by its primary keys: ['id'].
	 */
	public static endpointV1SubgenresIdPatch<ThrowOnError extends boolean = false>(
		options: Options<EndpointV1SubgenresIdPatchData, ThrowOnError>
	) {
		return (options?.client ?? client).patch<
			ThrowOnError,
			EndpointV1SubgenresIdPatchResponse,
			EndpointV1SubgenresIdPatchError
		>({
			...options,
			url: '/v1/subgenres/{id}'
		});
	}

	/**
	 * Endpoint
	 * Soft delete a Subgenre row from the database by its primary keys: ['id'].
	 */
	public static endpointV1SubgenresIdDelete<ThrowOnError extends boolean = false>(
		options: Options<EndpointV1SubgenresIdDeleteData, ThrowOnError>
	) {
		return (options?.client ?? client).delete<
			ThrowOnError,
			EndpointV1SubgenresIdDeleteResponse,
			EndpointV1SubgenresIdDeleteError
		>({
			...options,
			url: '/v1/subgenres/{id}'
		});
	}
}

export class ReleasesService {
	/**
	 * Endpoint
	 * Create a new Release row in the database.
	 */
	public static endpointV1ReleasesPost<ThrowOnError extends boolean = false>(
		options: Options<EndpointV1ReleasesPostData, ThrowOnError>
	) {
		return (options?.client ?? client).post<
			ThrowOnError,
			EndpointV1ReleasesPostResponse,
			EndpointV1ReleasesPostError
		>({
			...options,
			url: '/v1/releases'
		});
	}

	/**
	 * Endpoint
	 * Read multiple Release rows from the database with a limit and an offset.
	 */
	public static endpointV1ReleasesGet<ThrowOnError extends boolean = false>(
		options?: Options<EndpointV1ReleasesGetData, ThrowOnError>
	) {
		return (options?.client ?? client).get<
			ThrowOnError,
			EndpointV1ReleasesGetResponse,
			EndpointV1ReleasesGetError
		>({
			...options,
			url: '/v1/releases'
		});
	}

	/**
	 * Endpoint
	 * Read a single Release row from the database by its primary keys: ['id'].
	 */
	public static endpointV1ReleasesIdGet<ThrowOnError extends boolean = false>(
		options: Options<EndpointV1ReleasesIdGetData, ThrowOnError>
	) {
		return (options?.client ?? client).get<
			ThrowOnError,
			EndpointV1ReleasesIdGetResponse,
			EndpointV1ReleasesIdGetError
		>({
			...options,
			url: '/v1/releases/{id}'
		});
	}

	/**
	 * Endpoint
	 * Update an existing Release row in the database by its primary keys: ['id'].
	 */
	public static endpointV1ReleasesIdPatch<ThrowOnError extends boolean = false>(
		options: Options<EndpointV1ReleasesIdPatchData, ThrowOnError>
	) {
		return (options?.client ?? client).patch<
			ThrowOnError,
			EndpointV1ReleasesIdPatchResponse,
			EndpointV1ReleasesIdPatchError
		>({
			...options,
			url: '/v1/releases/{id}'
		});
	}

	/**
	 * Endpoint
	 * Soft delete a Release row from the database by its primary keys: ['id'].
	 */
	public static endpointV1ReleasesIdDelete<ThrowOnError extends boolean = false>(
		options: Options<EndpointV1ReleasesIdDeleteData, ThrowOnError>
	) {
		return (options?.client ?? client).delete<
			ThrowOnError,
			EndpointV1ReleasesIdDeleteResponse,
			EndpointV1ReleasesIdDeleteError
		>({
			...options,
			url: '/v1/releases/{id}'
		});
	}
}

export class LabelsService {
	/**
	 * Endpoint
	 * Create a new Label row in the database.
	 */
	public static endpointV1LabelsPost<ThrowOnError extends boolean = false>(
		options: Options<EndpointV1LabelsPostData, ThrowOnError>
	) {
		return (options?.client ?? client).post<
			ThrowOnError,
			EndpointV1LabelsPostResponse,
			EndpointV1LabelsPostError
		>({
			...options,
			url: '/v1/labels'
		});
	}

	/**
	 * Endpoint
	 * Read multiple Label rows from the database with a limit and an offset.
	 */
	public static endpointV1LabelsGet<ThrowOnError extends boolean = false>(
		options?: Options<EndpointV1LabelsGetData, ThrowOnError>
	) {
		return (options?.client ?? client).get<
			ThrowOnError,
			EndpointV1LabelsGetResponse,
			EndpointV1LabelsGetError
		>({
			...options,
			url: '/v1/labels'
		});
	}

	/**
	 * Endpoint
	 * Read a single Label row from the database by its primary keys: ['id'].
	 */
	public static endpointV1LabelsIdGet<ThrowOnError extends boolean = false>(
		options: Options<EndpointV1LabelsIdGetData, ThrowOnError>
	) {
		return (options?.client ?? client).get<
			ThrowOnError,
			EndpointV1LabelsIdGetResponse,
			EndpointV1LabelsIdGetError
		>({
			...options,
			url: '/v1/labels/{id}'
		});
	}

	/**
	 * Endpoint
	 * Update an existing Label row in the database by its primary keys: ['id'].
	 */
	public static endpointV1LabelsIdPatch<ThrowOnError extends boolean = false>(
		options: Options<EndpointV1LabelsIdPatchData, ThrowOnError>
	) {
		return (options?.client ?? client).patch<
			ThrowOnError,
			EndpointV1LabelsIdPatchResponse,
			EndpointV1LabelsIdPatchError
		>({
			...options,
			url: '/v1/labels/{id}'
		});
	}

	/**
	 * Endpoint
	 * Soft delete a Label row from the database by its primary keys: ['id'].
	 */
	public static endpointV1LabelsIdDelete<ThrowOnError extends boolean = false>(
		options: Options<EndpointV1LabelsIdDeleteData, ThrowOnError>
	) {
		return (options?.client ?? client).delete<
			ThrowOnError,
			EndpointV1LabelsIdDeleteResponse,
			EndpointV1LabelsIdDeleteError
		>({
			...options,
			url: '/v1/labels/{id}'
		});
	}
}
