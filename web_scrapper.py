from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

"""
Los comentarios estan en los elementos span del html
que tengan la clase "_2EO0yd2j", ejemplo:
<span class="_2EO0yd2j">Comentarios</span>
"""

""" 
Las puntuaciones las podemos encontrar en los 
aria-label de los elementos div que tengan uno 
de los siguientes atributos:
1 estrella: aria-label="1puntuación"
2 estrellas: aria-label="2puntuación"
3 estrellas: aria-label="3puntuación"
4 estrellas: aria-label="4puntuación"
5 estrellas: aria-label="5puntuación"
"""

"""
para cada comentario, obtener el texto y la puntuación
"""


def get_html(url):
    browser = webdriver.Firefox()
    browser.get(url)
    html = browser.page_source
    browser.quit()
    return html


def get_comments(html):
    soup = BeautifulSoup(html, "html.parser")
    comments = soup.find_all("span", class_="_2EO0yd2j")
    puntuaciones = []
    divs = soup.find_all(
        "div",
        {
            "aria-label": [
                "1puntuación",
                "2puntuación",
                "3puntuación",
                "4puntuación",
                "5puntuación",
            ]
        },
    )
    for div in divs:
        puntuacion = div["aria-label"]
        if (
            puntuacion == "1puntuación"
            or puntuacion == "2puntuación"
            or puntuacion == "3puntuación"
        ):
            puntuaciones.append(0)
        elif puntuacion == "4puntuación" or puntuacion == "5puntuación":
            puntuaciones.append(1)

    result = []
    for i in range(len(comments)):
        result.append({"text": comments[i].text, "puntuacion": puntuaciones[i]})

    return result


if __name__ == "__main__":
    urls = [
        "https://www.temu.com/mx/2pcs-juego-de-destornilladores-en-forma-de-cruz-destornillador-pequeno-para-electrodomesticos-y-juguetes-herramientas-manuales-g-601099532327275.html?_oak_mp_inf=EOuy5aCm1ogBGhQzd3U1MG5nZjhyOXY0OWdidzF0diD1kL3U6TE%3D&top_gallery_url=https%3A%2F%2Fimg.kwcdn.com%2Fproduct%2FFancyalgo%2FVirtualModelMatting%2Fda24075d39caeb1d1aba0c22604a5f54.jpg&spec_gallery_id=2052556935&refer_page_sn=10132&refer_source=0&freesia_scene=311&_oak_freesia_scene=311&_oak_rec_ext_1=MTE1MQ&refer_page_el_sn=207153&_x_channel_scene=spike&_x_channel_src=1&_x_sessn_id=sy8wy9wr8c&refer_page_name=lightning-deals&refer_page_id=10132_1711990066520_cnca9w9mw6&no_cache_id=g0w22",
        "https://www.temu.com/mx/cinta-metrica-de-acero-fluorescente-de-bloqueo-automatico-regla-de-caja-de-codigo-de-inyeccion-laser-de-alta-precision-herramienta-de-medicion-regla-ancha-1-ud-g-601099526475107.html?_oak_mp_inf=EOOagJ6m1ogBGhZnb29kc190cjk5MnNfcmVjb21tZW5kIIig69TpMQ%3D%3D&top_gallery_url=https%3A%2F%2Fimg.kwcdn.com%2Fproduct%2FFancyalgo%2FVirtualModelMatting%2F6e487a61853277a9eec03c8a4c41ece7.jpg&spec_gallery_id=2044871440&refer_page_sn=10017&refer_source=10016&freesia_scene=11&_oak_freesia_scene=11&_oak_rec_ext_1=NjYyNA&refer_page_el_sn=200444&refer_page_name=bgn_verification&refer_page_id=10017_1711998843014_6qimmw4kwa&_x_channel_scene=spike&_x_channel_src=1&_x_sessn_id=sy8wy9wr8c",
        "https://www.temu.com/mx/botas-de-invierno-termicas-de-cuero-para-hombre-con-cordones-zapatos-casuales-para-caminar-g-601099522460066.html?_oak_mp_inf=EKKTi5ym1ogBGi5jYXRlZ29yeV9saXN0XzY2OTM3ZDQwZTBjYjQ0NDhiNDAwMGJiN2E3YTA3MzlmINmE2djpMQ%3D%3D&top_gallery_url=https%3A%2F%2Fimg.kwcdn.com%2Fproduct%2FFancyalgo%2FVirtualModelMatting%2F3ff75fc9f850c5ff80b4acc5372a7b3a.jpg&spec_gallery_id=2015950053&refer_page_sn=10012&refer_source=0&freesia_scene=3&_oak_freesia_scene=3&_oak_rec_ext_1=NTE3NDE&refer_page_el_sn=200064&_x_enter_scene_type=cate_tab&_x_channel_scene=spike&_x_channel_src=1&_x_sessn_id=sy8wy9wr8c&refer_page_name=category&refer_page_id=10012_1711998912201_nph0ka46pt",
        "https://www.temu.com/mx/recargable-aspiradora-inalambrica-de-mano-bateria-de-1200mah-carga-usb-cartucho-de-filtro-reutilizable-para-limpieza-de-coches-g-601099531429352.html?_oak_mp_inf=EOjLrqCm1ogBGhhiZXN0X3NlbGxlcnNfbGlzdF9zMjU1M3Qg%2Bs3b2Okx&top_gallery_url=https%3A%2F%2Fimg.kwcdn.com%2Fproduct%2FFancyalgo%2FVirtualModelMatting%2F3baee6f9311d7924025424827cb66b10.jpg&spec_gallery_id=2056326047&refer_page_sn=10125&refer_source=0&freesia_scene=114&_oak_freesia_scene=114&_oak_rec_ext_1=MTI5NTg&refer_page_el_sn=201345&_x_enter_scene_type=cate_tab&_x_channel_scene=spike&_x_channel_src=1&_x_sessn_id=sy8wy9wr8c&refer_page_name=best_sellers&refer_page_id=10125_1711998954564_41j832lt6f",
        "https://www.temu.com/mx/linterna-led-de-1-pieza-linterna-potente-de-4-led-con-luz-lateral-cob-linterna-led-recargable-usb-de-4-modos-linterna-de-bateria-incorporada-impermeable-herramienta-de-camping-g-601099512449993.html?_oak_mp_inf=EMmXqJem1ogBGhZnb29kc19td2dkcGVfcmVjb21tZW5kIIyE3NjpMQ%3D%3D&top_gallery_url=https%3A%2F%2Fimg.kwcdn.com%2Fproduct%2FFancyalgo%2FVirtualModelMatting%2F0f36d327ab1fe66c2560d69cfe5b2baf.jpg&spec_gallery_id=10382391&refer_page_sn=10032&refer_source=10016&freesia_scene=11&_oak_freesia_scene=11&_oak_rec_ext_1=OTg5OA&refer_page_el_sn=200444&_x_enter_scene_type=cate_tab&_x_channel_scene=spike&_x_channel_src=1&_x_sessn_id=sy8wy9wr8c&refer_page_name=goods&refer_page_id=10032_1711998958892_rykp5w5mkl",
        "https://www.temu.com/mx/bomba-de-aire-para-automovil-pantalla-digital-inflador-de-neumaticos-electrico-portatil-de-12v-compresor-de-aire-multifuncion-para-automovil-g-601099517669593.html?_oak_mp_inf=ENnh5pmm1ogBGi5jYXRlZ29yeV9saXN0X2I3YjkzNzgzNjVlYjRlOTY4ODZhMzJjNmZkODE0Yzk5IL3m3djpMQ%3D%3D&top_gallery_url=https%3A%2F%2Fimg.kwcdn.com%2Fproduct%2FFancyalgo%2FVirtualModelMatting%2F9d0eb3a077ab1800857dcd671c832f44.jpg&spec_gallery_id=2005486954&refer_page_sn=10012&refer_source=0&freesia_scene=3&_oak_freesia_scene=3&_oak_rec_ext_1=MzM4Mjg&refer_page_el_sn=200064&_x_enter_scene_type=cate_tab&_x_channel_scene=spike&_x_channel_src=1&_x_sessn_id=sy8wy9wr8c&refer_page_name=category&refer_page_id=10012_1711998990370_hshfh7vfxa",
        "https://www.temu.com/mx/1-unidad-manguera-multiusos-manguera-de-jardin-mangueras-de-plastico-expandibles-manguera-de-agua-flexible-manguera-de-agua-para-lavado-de-autos-rociador-de-jardin-7-62-metros-15-24-metros-22-86-metros-30-48-metros-x-7-62-10-16-cm-herramientas-de-riego-suministros-de-limpieza-accesorios-de-limpieza-elementos-esenciales-del-apartamento-listo-para-la-escuela-g-601099520838471.html?_oak_mp_inf=EMeWqJum1ogBGhZnb29kc194NTBqaHVfcmVjb21tZW5kIKuU3tjpMQ%3D%3D&top_gallery_url=https%3A%2F%2Fimg.kwcdn.com%2Fproduct%2Ffancy%2F60cdb559-7ecc-437c-9131-9043144dced7.jpg&spec_gallery_id=2015386825&refer_page_sn=10032&refer_source=10016&freesia_scene=11&_oak_freesia_scene=11&_oak_rec_ext_1=ODU0Nw&refer_page_el_sn=200444&_x_enter_scene_type=cate_tab&_x_channel_scene=spike&_x_channel_src=1&_x_sessn_id=sy8wy9wr8c&refer_page_name=goods&refer_page_id=10032_1711998993986_rons6lu46q",
        "https://www.temu.com/mx/juguete-de-carro-de-control-remoto-de-la-serie-de-excavadoras-de-aleacion-de-ingenieria-para-ninos-g-601099542000559.html?_oak_mp_inf=EK%2Fns6Wm1ogBGhZnb29kc190NWY1OHNfcmVjb21tZW5kIKuT39jpMQ%3D%3D&top_gallery_url=https%3A%2F%2Fimg.kwcdn.com%2Fproduct%2Ffancy%2F27a49518-2dea-4f22-9eb1-042e4a730b87.jpg&spec_gallery_id=2093630565&refer_page_sn=10032&refer_source=10016&freesia_scene=11&_oak_freesia_scene=11&_oak_rec_ext_1=NTQwNDg&refer_page_el_sn=200444&_x_enter_scene_type=cate_tab&_x_channel_scene=spike&_x_channel_src=1&_x_sessn_id=sy8wy9wr8c&refer_page_name=goods&refer_page_id=10032_1711999010104_ogcq31w2qa",
        "https://www.temu.com/goods.html?_bg_fs=1&goods_id=601099538538722&_oak_mp_inf=EOLB4KOm1ogBGhZnb29kc19raXB2aWFfcmVjb21tZW5kIKWU4NjpMQ%3D%3D&top_gallery_url=https%3A%2F%2Fimg.kwcdn.com%2Fproduct%2FFancyalgo%2FVirtualModelMatting%2F33a2c8e46aa93d7df9f896fe16d834e8.jpg&spec_gallery_id=2067307607&refer_page_sn=10032&refer_source=10016&freesia_scene=11&_oak_freesia_scene=11&_oak_rec_ext_1=OTc0OA&refer_page_el_sn=200444&_x_enter_scene_type=cate_tab&_x_channel_scene=spike&_x_channel_src=1&_x_sessn_id=sy8wy9wr8c&refer_page_name=goods&refer_page_id=10032_1711999026714_q8y2n39pxh",
        "https://www.temu.com/mx/enfriador-de-aire-portatil-con-humidificador-de-niebla-un-gadget-fresco-para-uso-en-el-hogar-en-verano-ventilador-alimentado-por-usb-g-601099541201496.html?_oak_mp_inf=ENiEg6Wm1ogBGhZnb29kc191ankzZ3JfcmVjb21tZW5kIKqO4djpMQ%3D%3D&top_gallery_url=https%3A%2F%2Fimg.kwcdn.com%2Fproduct%2Fopen%2F2023-12-30%2F1703926664318-27e433acb4054d0481b5e9cf7d38f927-goods.jpeg&spec_gallery_id=2075396905&refer_page_sn=10032&refer_source=10016&freesia_scene=11&_oak_freesia_scene=11&_oak_rec_ext_1=MTM0MDg&refer_page_el_sn=200444&_x_enter_scene_type=cate_tab&_x_channel_scene=spike&_x_channel_src=1&_x_sessn_id=sy8wy9wr8c&refer_page_name=goods&refer_page_id=10032_1711999041796_e76dn53iyp",
    ]

    # malas
    """ (hay que hacer click en mostrar mas y luego hacer scroll)
    https://www.temu.com/mx/cama-plegable-para-acampar-con-cojin-y-almohada-cama-portatil-para-dormir-cama-ligera-con-bolsa-de-transporte-soporta-149-69-kg-g-601099543816233.html?_oak_mp_inf=EKnQoqam1ogBGhVqNWxkOG91Y3dpazlvNjFzbWpoem8g5r7l2Okx&top_gallery_url=https%3A%2F%2Fimg.kwcdn.com%2Fproduct%2Ffancy%2Fbe59289f-0832-4356-82ce-cefbceb98149.jpg&spec_gallery_id=2091790002&refer_page_sn=10005&refer_source=0&freesia_scene=1&_oak_freesia_scene=1&_oak_rec_ext_1=ODYzOTg&refer_page_el_sn=200024&_x_enter_scene_type=cate_tab&_x_channel_scene=spike&_x_channel_src=1&_x_sessn_id=sy8wy9wr8c&refer_page_name=home&refer_page_id=10005_1711999114414_wz78tm6s28
    https://www.temu.com/mx/1-pieza-colchon-delgado-de-espuma-viscoelastica-con-bucle-de-carbon-de-bambu-almohadilla-de-espuma-de-carbon-de-bambu-infusionada-con-espuma-viscoelastica-para-aliviar-la-presion-g-601099543292802.html?_oak_mp_inf=EILXgqam1ogBGhZnb29kc19mejl1a2lfcmVjb21tZW5kIKeg6djpMQ%3D%3D&top_gallery_url=https%3A%2F%2Fimg.kwcdn.com%2Fproduct%2Ffancy%2Fa2ff5d43-b13a-461d-8627-07d1fde59628.jpg&spec_gallery_id=2082588681&refer_page_sn=10032&refer_source=10016&freesia_scene=11&_oak_freesia_scene=11&_oak_rec_ext_1=ODcwNzk&refer_page_el_sn=200444&_x_enter_scene_type=cate_tab&_x_channel_scene=spike&_x_channel_src=1&_x_sessn_id=sy8wy9wr8c&refer_page_name=goods&refer_page_id=10032_1711999174977_iqys8lk526
    https://www.temu.com/mx/cama-plegable-portatil-para-dormir-cama-plegable-para-exteriores-adecuada-para-jugar-en-la-playa-acampar-y-hacer-picnic-siesta-en-la-oficina-g-601099525390826.html?_oak_mp_inf=EOqDvp2m1ogBGhZnb29kc19sYnJyZTlfcmVjb21tZW5kIOKD99jpMQ%3D%3D&top_gallery_url=https%3A%2F%2Fimg.kwcdn.com%2Fproduct%2FFancyalgo%2FVirtualModelMatting%2F9c00df328cd4e087aaae79756b631199.jpg&spec_gallery_id=2031650861&refer_page_sn=10032&refer_source=10016&freesia_scene=11&_oak_freesia_scene=11&_oak_rec_ext_1=MTk0NzQ4&refer_page_el_sn=200444&_x_enter_scene_type=cate_tab&_x_channel_scene=spike&_x_channel_src=1&_x_sessn_id=sy8wy9wr8c&refer_page_name=goods&refer_page_id=10032_1711999401360_u8zd945x9h
    """

    html = get_html(
        "https://www.temu.com/mx/2pcs-juego-de-destornilladores-en-forma-de-cruz-destornillador-pequeno-para-electrodomesticos-y-juguetes-herramientas-manuales-g-601099532327275.html?_oak_mp_inf=EOuy5aCm1ogBGhQzd3U1MG5nZjhyOXY0OWdidzF0diD1kL3U6TE%3D&top_gallery_url=https%3A%2F%2Fimg.kwcdn.com%2Fproduct%2FFancyalgo%2FVirtualModelMatting%2Fda24075d39caeb1d1aba0c22604a5f54.jpg&spec_gallery_id=2052556935&refer_page_sn=10132&refer_source=0&freesia_scene=311&_oak_freesia_scene=311&_oak_rec_ext_1=MTE1MQ&refer_page_el_sn=207153&_x_channel_scene=spike&_x_channel_src=1&_x_sessn_id=sy8wy9wr8c&refer_page_name=lightning-deals&refer_page_id=10132_1711990066520_cnca9w9mw6&no_cache_id=g0w22"
    )

    comments = get_comments(html)

    print("-" * 50)
    print("Comments:")
    for comment in comments:
        print(comment)
    print("-" * 50)
