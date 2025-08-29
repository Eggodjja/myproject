--
-- PostgreSQL database dump
--

-- Dumped from database version 16.9 (Ubuntu 16.9-0ubuntu0.24.04.1)
-- Dumped by pg_dump version 16.9 (Ubuntu 16.9-0ubuntu0.24.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: post; Type: TABLE; Schema: public; Owner: s1319
--

CREATE TABLE public.post (
    id integer NOT NULL,
    first_name character varying(250),
    last_name character varying(250),
    email character varying(250)
);


ALTER TABLE public.post OWNER TO s1319;

--
-- Name: post_id_seq; Type: SEQUENCE; Schema: public; Owner: s1319
--

CREATE SEQUENCE public.post_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.post_id_seq OWNER TO s1319;

--
-- Name: post_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: s1319
--

ALTER SEQUENCE public.post_id_seq OWNED BY public.post.id;


--
-- Name: post id; Type: DEFAULT; Schema: public; Owner: s1319
--

ALTER TABLE ONLY public.post ALTER COLUMN id SET DEFAULT nextval('public.post_id_seq'::regclass);


--
-- Data for Name: post; Type: TABLE DATA; Schema: public; Owner: s1319
--

COPY public.post (id, first_name, last_name, email) FROM stdin;
40	Egor 	Semenenko	s1319941@gmail.com
\.


--
-- Name: post_id_seq; Type: SEQUENCE SET; Schema: public; Owner: s1319
--

SELECT pg_catalog.setval('public.post_id_seq', 40, true);


--
-- Name: post post_pkey; Type: CONSTRAINT; Schema: public; Owner: s1319
--

ALTER TABLE ONLY public.post
    ADD CONSTRAINT post_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

