/* USER CODE BEGIN Header */
/**
  ******************************************************************************
  * @file           : main.h
  * @brief          : Header for main.c file.
  *                   This file contains the common defines of the application.
  ******************************************************************************
  * @attention
  *
  * Copyright (c) 2024 STMicroelectronics.
  * All rights reserved.
  *
  * This software is licensed under terms that can be found in the LICENSE file
  * in the root directory of this software component.
  * If no LICENSE file comes with this software, it is provided AS-IS.
  *
  ******************************************************************************
  */
/* USER CODE END Header */

/* Define to prevent recursive inclusion -------------------------------------*/
#ifndef __MAIN_H
#define __MAIN_H

#ifdef __cplusplus
extern "C" {
#endif

/* Includes ------------------------------------------------------------------*/
#include "stm32f4xx_hal.h"

/* Private includes ----------------------------------------------------------*/
/* USER CODE BEGIN Includes */

/* USER CODE END Includes */

/* Exported types ------------------------------------------------------------*/
/* USER CODE BEGIN ET */

/* USER CODE END ET */

/* Exported constants --------------------------------------------------------*/
/* USER CODE BEGIN EC */

/* USER CODE END EC */

/* Exported macro ------------------------------------------------------------*/
/* USER CODE BEGIN EM */

#define IMAGE_WIDTH  160
#define IMAGE_HEIGHT 120
#define FRAME_BUFFER 0x080E0000

#define OV7670_ADDR 0x42

#define COM3_ADDR 0x0C
#define COM3_ZOOM 0x08
#define COM3_DCW_PCLK 0x10

#define COM14_ADDR 0x3E
#define COM14_QVGA 3
#define COM14_SCALE_ENABLE 0x08

#define COM15_ADDR 0x40
#define COM15_RGB565 0x10

#define COM7_ADDR 0x12
#define COM7_QVGA 0x10
#define COM7_RGB 0x04

#define SCALING_DCW_CTR 0x72
#define SCALING_DCW_CTR_DSH2 0x01
#define SCALING_DCW_CTR_DSV2 0x10
#define SCALING_DCW_CTR_DSH4 0x02
#define SCALING_DCW_CTR_DSV4 0x20

/* USER CODE END EM */

/* Exported functions prototypes ---------------------------------------------*/
void Error_Handler(void);

/* USER CODE BEGIN EFP */

/* USER CODE END EFP */

/* Private defines -----------------------------------------------------------*/
#define HREF_Pin GPIO_PIN_13
#define HREF_GPIO_Port GPIOC
#define LED_Pin GPIO_PIN_1
#define LED_GPIO_Port GPIOA
#define XCLCK_Pin GPIO_PIN_5
#define XCLCK_GPIO_Port GPIOA
#define BUTTON_Pin GPIO_PIN_15
#define BUTTON_GPIO_Port GPIOA
#define SCL_Pin GPIO_PIN_8
#define SCL_GPIO_Port GPIOB
#define SDA_Pin GPIO_PIN_9
#define SDA_GPIO_Port GPIOB

/* USER CODE BEGIN Private defines */

/* USER CODE END Private defines */

#ifdef __cplusplus
}
#endif

#endif /* __MAIN_H */
